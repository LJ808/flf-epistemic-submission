#!/usr/bin/env python3
"""
E-Prime Ingestion Tool — FLF Submission
=========================================

QUICK START (one command, after setting your API key):

    pip install -r requirements.txt
    export ANTHROPIC_API_KEY=your_key_here
    python3 ingest.py "There is a positive association between egg consumption and CVD risk"

Fixed-prompt ingestion: takes a source claim and produces an E-Prime rewrite
in YAML-formatted claim record matching the vault schema used throughout
flf-vault/CLAIMS/. Same prompt, zero per-source tuning — this is the
mechanical layer that produced all nine claim records in this vault.

No API key? Run with --demo to see a pre-recorded example output instead
of making a live API call.
"""

import argparse
import os
import re
import sys

import yaml

# The fixed ingestion prompt — identical for every source, every case.
FIXED_PROMPT = """You are an E-Prime ingestion system. Given an original claim or quote from a source, produce:

1. An E-Prime rewrite that eliminates "is/are/was/were/be/being/been" and forces numerical/structural specificity
2. Analysis of what the rewrite exposes that the original hid
3. Ambiguity flags — gaps that neither the original nor the rewrite resolve
4. Adversarial Interpretation — how a motivated reader could misuse this claim despite the rewrite

Output as valid YAML only. No markdown fences. No preamble.

Schema:
-------
original_quote: |
  [verbatim source text]

e_prime_rewrite: |
  [rewritten without any form of "to be", with numbers and specifics forced into view]

analysis: |
  [2-3 sentences: what does the rewrite expose? what was hidden in "is"? what gap does it reveal?]

ambiguity_flags: |
  [What questions remain even after the rewrite? What information is still missing from the source?]

adversarial_interpretation: |
  [How could a motivated reader misuse this claim despite the rewrite? What attack surface remains?]

confidence_assessment: |
  [Integer 1-5. 5 = motivated misreading now requires visibly adding language. 1 = rewrite barely changes readability.]
"""

DEMO_OUTPUT = {
    "original_quote": "There is a dose-response positive association between egg consumption and the risk of CVD and diabetes",
    "e_prime_rewrite": "Egg intake correlates with CVD risk at RR 1.19 (CI 1.02-1.38) and diabetes at RR 1.68 (CI 1.41-2.00), pooled across 14 studies, n=320,778.",
    "analysis": "The rewrite forces a number into a sentence that originally needed none. 'There is an association' cannot survive E-Prime without specifying direction, magnitude, and confidence interval, which become mandatory rather than optional once 'is' disappears.",
    "ambiguity_flags": "'Association' leaves causal direction unaddressed -- neither the source nor the rewrite resolves whether egg consumption causes CVD or reflects a shared upstream factor.",
    "adversarial_interpretation": "A reader motivated to dismiss this finding could note the pooled analysis lacks the same covariate adjustment as competing cohort studies. A reader motivated to accept it could ignore that 'dose-response' oversells what a highest-vs-lowest comparison shows.",
    "confidence_assessment": 4,
}


def strip_markdown_fences(text: str) -> str:
    """Defensively strip a fenced-code wrapper (triple backtick + optional yaml tag)
    if the model adds one despite the prompt explicitly forbidding it. No-op on
    already-clean YAML."""
    text = text.strip()
    match = re.match(r"^```(?:yaml|yml)?\s*\n(.*?)\n```\s*$", text, re.DOTALL)
    if match:
        return match.group(1)
    return text


def ingest_claim(source_text: str) -> dict:
    """Run the fixed ingestion prompt against source text via the Anthropic API."""
    try:
        import anthropic
    except ImportError:
        print(
            "Missing dependency. Run: pip install -r requirements.txt",
            file=sys.stderr,
        )
        sys.exit(1)

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print(
            "No ANTHROPIC_API_KEY set. Run with --demo to see example output "
            "without an API key, or set:\n  export ANTHROPIC_API_KEY=your_key_here",
            file=sys.stderr,
        )
        sys.exit(1)

    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"{FIXED_PROMPT}\n\nSource claim to ingest:\n\n{source_text}",
            }
        ],
    )

    response_text = message.content[0].text
    cleaned_text = strip_markdown_fences(response_text)

    try:
        result = yaml.safe_load(cleaned_text)
    except yaml.YAMLError as e:
        print(f"YAML parse error even after fence-stripping: {e}", file=sys.stderr)
        print(f"Raw model response (unmodified):\n{response_text}", file=sys.stderr)
        print(
            "\nThe model didn't return parseable YAML. Try re-running -- "
            "this is a model-output issue, not a script bug.",
            file=sys.stderr,
        )
        sys.exit(1)

    if not isinstance(result, dict):
        print(
            f"Parsed YAML but got {type(result).__name__}, not a dict. "
            f"Raw model response:\n{response_text}",
            file=sys.stderr,
        )
        sys.exit(1)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="E-Prime ingestion: fixed-prompt claim extraction matching the flf-vault schema."
    )
    parser.add_argument(
        "source_text",
        nargs="?",
        help="The original claim or quote to ingest (wrap in quotes).",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Print a pre-recorded example output without calling the API (no key needed).",
    )
    args = parser.parse_args()

    if args.demo:
        print(yaml.dump(DEMO_OUTPUT, default_flow_style=False, sort_keys=False))
        return

    if not args.source_text:
        parser.print_help()
        sys.exit(1)

    print("Running E-Prime ingestion...", file=sys.stderr)
    claim_data = ingest_claim(args.source_text)
    print(yaml.dump(claim_data, default_flow_style=False, sort_keys=False))


if __name__ == "__main__":
    main()
