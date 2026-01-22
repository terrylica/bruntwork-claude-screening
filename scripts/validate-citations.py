#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pydantic>=2.0",
# ]
# ///
"""
Validate citations in quiz JSON files.

Checks:
- All questions have at least one citation for correctAnswer
- All citations have required fields (source, authority, quotedText)
- Authority tiers are valid (1, 2, or 3)
- Access dates are within 90 days (warning if stale)
- File URLs are accessible (file:// protocol)

Usage:
    uv run scripts/validate-citations.py           # Validate all quizzes
    uv run scripts/validate-citations.py --strict  # Fail on warnings too
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

from pydantic import BaseModel, ValidationError

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
QUIZ_DIR = PROJECT_DIR / "quiz-data"


class Source(BaseModel):
    """Citation source metadata."""

    type: str
    title: str
    url: str
    section: str | None = None
    accessDate: str


class Authority(BaseModel):
    """Citation authority level."""

    tier: int
    organization: str
    confidence: float


class Citation(BaseModel):
    """Single citation reference."""

    source: Source
    authority: Authority
    quotedText: str
    context: str | None = None


class CitationResult:
    """Result of citation validation."""

    def __init__(self, quiz_file: str):
        self.quiz_file = quiz_file
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.questions_checked = 0
        self.citations_found = 0


def expand_path(url: str) -> str:
    """Expand ~ and environment variables in file:// URLs."""
    if url.startswith("file://"):
        path = url[7:]  # Remove file://
        path = os.path.expanduser(path)
        path = os.path.expandvars(path)
        return path
    return url


def validate_file_url(url: str) -> tuple[bool, str]:
    """Check if a file:// URL points to an accessible file."""
    if not url.startswith("file://"):
        return True, ""  # Not a file URL, skip check

    path = expand_path(url)
    if not os.path.exists(path):
        return False, f"File not found: {path}"
    return True, ""


def validate_access_date(date_str: str, stale_days: int = 90) -> tuple[bool, str]:
    """Check if access date is within acceptable range."""
    try:
        access_date = datetime.strptime(date_str, "%Y-%m-%d")
        cutoff = datetime.now() - timedelta(days=stale_days)
        if access_date < cutoff:
            return False, f"Access date {date_str} is more than {stale_days} days old"
        return True, ""
    except ValueError:
        return False, f"Invalid date format: {date_str} (expected YYYY-MM-DD)"


def validate_citation(citation_data: dict, question_num: int, result: CitationResult):
    """Validate a single citation."""
    try:
        citation = Citation(**citation_data)
        result.citations_found += 1

        # Validate authority tier
        if citation.authority.tier not in [1, 2, 3]:
            result.errors.append(
                f"Q{question_num}: Invalid authority tier {citation.authority.tier} (must be 1-3)"
            )

        # Validate confidence
        if not (0.0 <= citation.authority.confidence <= 1.0):
            result.errors.append(
                f"Q{question_num}: Invalid confidence {citation.authority.confidence} (must be 0.0-1.0)"
            )

        # Validate file URL accessibility
        valid, msg = validate_file_url(citation.source.url)
        if not valid:
            result.warnings.append(f"Q{question_num}: {msg}")

        # Check access date freshness
        valid, msg = validate_access_date(citation.source.accessDate)
        if not valid:
            result.warnings.append(f"Q{question_num}: {msg}")

        # Check quotedText is not empty
        if not citation.quotedText.strip():
            result.errors.append(f"Q{question_num}: Empty quotedText")

    except ValidationError as e:
        for error in e.errors():
            field = ".".join(str(x) for x in error["loc"])
            result.errors.append(f"Q{question_num}: Citation field '{field}': {error['msg']}")


def validate_quiz_citations(quiz_path: Path) -> CitationResult:
    """Validate all citations in a quiz file."""
    result = CitationResult(quiz_path.name)

    with open(quiz_path) as f:
        quiz_data = json.load(f)

    questions = quiz_data.get("questions", [])

    for q in questions:
        q_num = q.get("questionNumber", "?")
        result.questions_checked += 1

        citations = q.get("citations", {})

        # Check for correctAnswer citations
        correct_citations = citations.get("correctAnswer", [])
        if not correct_citations:
            result.warnings.append(f"Q{q_num}: No citation for correctAnswer")
        else:
            for citation_data in correct_citations:
                validate_citation(citation_data, q_num, result)

        # Validate incorrectOptions citations if present
        incorrect_citations = citations.get("incorrectOptions", {})
        for _opt_idx, opt_citations in incorrect_citations.items():
            for citation_data in opt_citations:
                validate_citation(citation_data, q_num, result)

    return result


def main():
    parser = argparse.ArgumentParser(description="Validate quiz citations")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings too")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed output")
    args = parser.parse_args()

    quiz_files = list(QUIZ_DIR.glob("*.json"))
    if not quiz_files:
        print("No quiz files found in quiz-data/")
        sys.exit(1)

    print(f"\nValidating citations in {len(quiz_files)} quiz files...\n")

    all_results = []
    total_errors = 0
    total_warnings = 0

    for quiz_path in sorted(quiz_files):
        result = validate_quiz_citations(quiz_path)
        all_results.append(result)
        total_errors += len(result.errors)
        total_warnings += len(result.warnings)

        # Status indicator
        if result.errors:
            status = "[FAIL]"
        elif result.warnings:
            status = "[WARN]"
        else:
            status = "[OK]"

        print(
            f"{status} {result.quiz_file}: "
            f"{result.questions_checked} questions, "
            f"{result.citations_found} citations"
        )

        if args.verbose and (result.errors or result.warnings):
            for err in result.errors:
                print(f"      ERROR: {err}")
            for warn in result.warnings:
                print(f"      WARN: {warn}")

    # Summary
    print("\n" + "=" * 60)
    print("CITATION VALIDATION SUMMARY")
    print("=" * 60)
    print(f"Total quizzes: {len(quiz_files)}")
    print(f"Total errors: {total_errors}")
    print(f"Total warnings: {total_warnings}")

    # Exit code
    if total_errors > 0:
        print("\nValidation FAILED - fix errors before proceeding")
        sys.exit(1)
    elif args.strict and total_warnings > 0:
        print("\nValidation FAILED (strict mode) - fix warnings before proceeding")
        sys.exit(1)
    else:
        print("\nValidation PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
