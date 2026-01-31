#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pydantic>=2.0"]
# ///
"""
Generate quiz review page from Single Source of Truth (SSoT).

Reads all quiz-data/*.json files and generates docs/review.md with:
- Full answer key with all options (correct marked)
- Explanations for each question
- Collapsible citations with authority tiers and confidence scores
- Table of contents and statistics

Usage:
    uv run scripts/generate-review-page.py
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

# Quiz file order (determines display order)
# v2.0: Consolidated into principle-based assessments
QUIZ_ORDER = [
    "effective-prompting.json",
    "safety-autonomy.json",
    "agents-deep-dive.json",
    "hooks-lifecycle.json",
    "integration-tools.json",
]


def load_all_quizzes(quiz_dir: Path) -> list[dict[str, Any]]:
    """Load all quiz JSON files in defined order."""
    quizzes = []
    for filename in QUIZ_ORDER:
        quiz_path = quiz_dir / filename
        if quiz_path.exists():
            with open(quiz_path) as f:
                quiz = json.load(f)
                quiz["_filename"] = filename
                quiz["_slug"] = filename.replace(".json", "")
                quizzes.append(quiz)
        else:
            print(f"Warning: {filename} not found")
    return quizzes


def generate_statistics(quizzes: list[dict]) -> dict:
    """Calculate statistics across all quizzes."""
    total_questions = 0
    tier_counts = {1: 0, 2: 0, 3: 0}
    citation_count = 0

    for quiz in quizzes:
        for question in quiz.get("questions", []):
            total_questions += 1
            citations = question.get("citations", {}).get("correctAnswer", [])
            if citations:
                citation_count += 1
                for citation in citations:
                    tier = citation.get("authority", {}).get("tier", 3)
                    tier_counts[tier] = tier_counts.get(tier, 0) + 1

    total_citations = sum(tier_counts.values())

    return {
        "total_questions": total_questions,
        "total_domains": len(quizzes),
        "citation_coverage": (citation_count / total_questions * 100) if total_questions > 0 else 0,
        "tier_breakdown": {
            f"Tier {tier}": (count / total_citations * 100) if total_citations > 0 else 0
            for tier, count in tier_counts.items()
        }
    }


def format_citation_block(citation: dict) -> str:
    """Format a single citation as an open details block with smaller font.

    Uses 'open' attribute to show expanded by default.
    Uses inline styles for smaller font size.
    """
    source = citation.get("source", {})
    authority = citation.get("authority", {})

    tier = authority.get("tier", 3)
    org = authority.get("organization", "Unknown")
    confidence = authority.get("confidence", 0)

    title = source.get("title", "Unknown Source")
    url = source.get("url", "")
    online_url = source.get("onlineUrl", "")
    section = source.get("section", "")
    access_date = source.get("accessDate", "")

    quoted_text = citation.get("quotedText", "")

    # Use onlineUrl for clickable link if available, otherwise show url as code
    if online_url and online_url.startswith("https://"):
        url_line = f'<a href="{online_url}">{title}</a>'
    elif url.startswith("https://"):
        url_line = f'<a href="{url}">{title}</a>'
    else:
        url_line = f"<code>{url}</code>"

    # Build HTML content with smaller font
    content_lines = [f"<strong>Source</strong>: {title}<br>"]
    content_lines.append(f"<strong>URL</strong>: {url_line}<br>")

    if section:
        content_lines.append(f"<strong>Section</strong>: {section}<br>")
    if access_date:
        content_lines.append(f"<strong>Access Date</strong>: {access_date}<br>")

    if quoted_text:
        content_lines.append(f'<blockquote style="font-size: 0.85em; margin: 0.5em 0;">"{quoted_text}"</blockquote>')

    content = "\n".join(content_lines)

    # 'open' attribute makes details expanded by default
    # 'citation' class provides styling via CSS block at top of page
    return f"""<details open class="citation">
<summary>Citation [Tier {tier} - {org}] ({confidence:.0%} confidence)</summary>

{content}

</details>"""


def format_question(question: dict, quiz_question_num: int) -> str:
    """Format a single question with options and citation."""
    q_text = question.get("questionText", "")
    options = question.get("options", [])
    correct_idx = question.get("correctAnswerIndex", 0)
    explanation = question.get("explanation", "")
    citations = question.get("citations", {}).get("correctAnswer", [])

    lines = [
        f"### Q{quiz_question_num + 1}. {q_text}",
        "",
        "| Option | |",
        "| ------ | --- |",
    ]

    for i, option in enumerate(options):
        letter = chr(65 + i)  # A, B, C, D...
        if i == correct_idx:
            lines.append(f"| **{letter}. {option}** | ✓ |")
        else:
            lines.append(f"| {letter}. {option} | |")

    lines.append("")

    if explanation:
        lines.append(f"**Explanation**: {explanation}")
        lines.append("")

    for citation in citations:
        lines.append(format_citation_block(citation))
        lines.append("")

    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def generate_toc(quizzes: list[dict]) -> str:
    """Generate table of contents."""
    lines = [
        "## Table of Contents",
        "",
        "| # | Domain | Questions | Weight | Jump |",
        "| - | ------ | --------- | ------ | ---- |",
    ]

    for i, quiz in enumerate(quizzes, 1):
        domain = quiz.get("domain", "Unknown")
        weight = quiz.get("weight", 0)
        num_questions = len(quiz.get("questions", []))
        slug = quiz.get("_slug", "")

        lines.append(f"| {i} | {domain} | {num_questions} | {weight:.0%} | [Go](#{slug}) |")

    lines.append("")
    return "\n".join(lines)


def generate_stats_table(stats: dict) -> str:
    """Generate statistics table."""
    lines = [
        "## Statistics",
        "",
        "| Metric | Value |",
        "| ------ | ----- |",
        f"| Total Questions | {stats['total_questions']} |",
        f"| Domains | {stats['total_domains']} |",
        f"| Citation Coverage | {stats['citation_coverage']:.0f}% |",
    ]

    for tier, pct in stats["tier_breakdown"].items():
        tier_label = {"Tier 1": "Tier 1 (Official)", "Tier 2": "Tier 2 (Internal)", "Tier 3": "Tier 3 (Community)"}.get(tier, tier)
        lines.append(f"| {tier_label} | {pct:.0f}% |")

    lines.append("")
    return "\n".join(lines)


def generate_quiz_section(quiz: dict) -> str:
    """Generate a complete quiz section."""
    title = quiz.get("title", "Unknown Quiz")
    domain = quiz.get("domain", "Unknown")
    weight = quiz.get("weight", 0)
    questions = quiz.get("questions", [])

    lines = [
        f"## {title.replace(' Assessment', '')}",
        "",
        f"*Domain: {domain} | Weight: {weight:.0%}*",
        "",
    ]

    for i, question in enumerate(questions):
        lines.append(format_question(question, i))

    return "\n".join(lines)


def generate_review_page(quizzes: list[dict]) -> str:
    """Generate the complete review page markdown."""
    stats = generate_statistics(quizzes)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # CSS for citation styling (inline styles stripped by Jekyll)
    css_block = """<style>
.citation {
  font-size: 0.8em;
  margin: 0.5em 0;
  padding: 0.75em;
  background: rgba(128,128,128,0.1);
  border-radius: 4px;
  border-left: 3px solid #666;
}
.citation summary {
  cursor: pointer;
  font-weight: 500;
  color: #888;
}
.citation blockquote {
  font-size: 0.95em;
  margin: 0.5em 0;
  font-style: italic;
}
</style>"""

    lines = [
        "---",
        "title: Quiz Answer Key & Review",
        "permalink: /review/",
        "toc: true",
        "toc_sticky: true",
        "---",
        "",
        css_block,
        "",
        "> This page contains all correct answers with explanations and authoritative citations.",
        "> Use this as a learning resource alongside the [assessment quizzes](./).",
        "",
        f"*Generated: {timestamp}*",
        "",
        "---",
        "",
        generate_stats_table(stats),
        "---",
        "",
        generate_toc(quizzes),
        "---",
        "",
    ]

    for quiz in quizzes:
        lines.append(generate_quiz_section(quiz))
        lines.append("")

    # Footer
    lines.extend([
        "---",
        "",
        "*This answer key is auto-generated from the [quiz source files](https://github.com/terrylica/bruntwork-claude-screening/tree/main/quiz-data).*",
        "",
    ])

    return "\n".join(lines)


def main():
    """Main entry point."""
    project_root = Path(__file__).parent.parent
    quiz_dir = project_root / "quiz-data"
    output_path = project_root / "docs" / "review.md"

    print(f"📚 Loading quizzes from {quiz_dir}...")
    quizzes = load_all_quizzes(quiz_dir)

    if not quizzes:
        print("❌ No quiz files found!")
        return 1

    print(f"✓ Loaded {len(quizzes)} quiz files")

    stats = generate_statistics(quizzes)
    print(f"  - {stats['total_questions']} questions")
    print(f"  - {stats['citation_coverage']:.0f}% citation coverage")

    print("\n📝 Generating review page...")
    content = generate_review_page(quizzes)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(content)

    print(f"✓ Written to {output_path}")
    print("\n🔗 Preview: cd docs && python -m http.server 8000")
    print("   Then visit: http://localhost:8000/review")

    return 0


if __name__ == "__main__":
    exit(main())
