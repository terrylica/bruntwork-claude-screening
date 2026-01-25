#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pydantic>=2.0"]
# ///
"""
Validate Claude Code quiz JSON files against schema.

Usage:
    uv run scripts/validate-quiz.py [--quiz QUIZ_NAME]
"""

import json
import sys
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, ValidationError


class Source(BaseModel):
    """Citation source schema."""

    type: str | None = None
    title: str
    url: str
    onlineUrl: str | None = None  # Optional public URL for review page
    section: str | None = None
    accessDate: str | None = None


class Authority(BaseModel):
    """Citation authority schema."""

    tier: int = Field(ge=1, le=3)
    organization: str
    confidence: float = Field(ge=0.0, le=1.0)


class Citation(BaseModel):
    """Citation schema."""

    source: Source
    authority: Authority
    quotedText: str
    context: str | None = None


class Citations(BaseModel):
    """Question citations schema."""

    question: list[Citation] | None = None
    correctAnswer: list[Citation] | None = None
    incorrectOptions: dict[str, list[Citation]] | None = None


class Question(BaseModel):
    """Quiz question schema."""

    questionNumber: int = Field(ge=0)
    questionText: str = Field(min_length=10)
    type: Literal["multiple_choice", "short_answer", "paragraph", "matching"]
    required: bool = True
    options: list[str] | None = None
    correctAnswerIndex: int | None = None
    correctAnswer: str | None = None
    explanation: str | None = None
    matchingPairs: list[dict] | None = None
    citations: Citations | None = None


class Quiz(BaseModel):
    """Quiz schema."""

    title: str = Field(min_length=5)
    description: str = Field(min_length=20)
    isQuiz: bool = True
    domain: str | None = None
    weight: float | None = Field(default=None, ge=0, le=1)
    questions: list[Question] = Field(min_length=1)


def validate_quiz_file(quiz_path: Path) -> tuple[bool, str]:
    """Validate a single quiz file."""
    try:
        with open(quiz_path) as f:
            data = json.load(f)

        quiz = Quiz.model_validate(data)

        # Additional validation
        for q in quiz.questions:
            if q.type == "multiple_choice":
                if not q.options or len(q.options) < 2:
                    return False, f"Question {q.questionNumber}: multiple_choice needs >= 2 options"
                if q.correctAnswerIndex is None:
                    return False, f"Question {q.questionNumber}: missing correctAnswerIndex"
                if q.correctAnswerIndex >= len(q.options):
                    return False, f"Question {q.questionNumber}: correctAnswerIndex out of range"

            elif q.type == "short_answer":
                if not q.correctAnswer:
                    return False, f"Question {q.questionNumber}: short_answer needs correctAnswer"

        return True, f"✓ Valid: {len(quiz.questions)} questions"

    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"
    except ValidationError as e:
        return False, f"Validation error: {e}"


def main():
    quiz_dir = Path(__file__).parent.parent / "quiz-data"
    log_dir = Path(__file__).parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)

    quiz_files = list(quiz_dir.glob("*.json"))

    if not quiz_files:
        print("❌ No quiz files found in quiz-data/")
        sys.exit(1)

    print(f"📚 Validating {len(quiz_files)} quiz files...\n")

    all_valid = True
    results = []

    for quiz_file in sorted(quiz_files):
        valid, message = validate_quiz_file(quiz_file)
        status = "✓" if valid else "✗"
        print(f"  {status} {quiz_file.name}: {message}")
        results.append({"file": quiz_file.name, "valid": valid, "message": message})

        if not valid:
            all_valid = False

    # Write log
    log_file = log_dir / "quiz-validation.log"
    with open(log_file, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n📝 Log written to {log_file}")

    if all_valid:
        print("\n✓ All quizzes valid!")
        sys.exit(0)
    else:
        print("\n✗ Some quizzes have errors")
        sys.exit(1)


if __name__ == "__main__":
    main()
