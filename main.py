"""Entry point: extract text from a document file and summarise it with Claude."""

import argparse
import sys
from pathlib import Path

import llm_client
from base_extractor import DocumentExtractor
from pdf_extractor import PdfExtractor
from ppt_extractor import PptExtractor
from word_extractor import WordExtractor

EXTRACTORS: list[DocumentExtractor] = [
    WordExtractor(),
    PdfExtractor(),
    PptExtractor(),
]


def find_extractor(path: Path) -> DocumentExtractor:
    for extractor in EXTRACTORS:
        if extractor.supports(path):
            return extractor
    supported = ", ".join(
        ext for e in EXTRACTORS for ext in e.supported_extensions
    )
    raise ValueError(
        f"No extractor found for '{path.suffix}'. Supported: {supported}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract text from a document and summarise it."
    )
    parser.add_argument("file", type=Path, help="Path to the document file.")
    parser.add_argument(
        "--no-summary",
        action="store_true",
        help="Skip the LLM summarisation step.",
    )
    args = parser.parse_args()

    path: Path = args.file.resolve()
    if not path.exists():
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    extractor = find_extractor(path)
    print(f"Extracting '{path.name}' using {type(extractor).__name__}...")
    document = extractor.extract(path)

    print(f"\nTitle   : {document.title}")
    print(f"Words   : {document.word_count()}")
    print(f"Metadata: {document.metadata}")
    print("\n--- Extracted text (first 500 chars) ---")
    print(document.text[:500])

    if not args.no_summary:
        if not llm_client._api_key_is_set():
            print(
                "\n[ANTHROPIC_API_KEY not set — skipping summarisation]",
                file=sys.stderr,
            )
            return
        print("\n--- LLM Summary ---")
        summary = llm_client.summarise(document)
        print(summary)


if __name__ == "__main__":
    main()
