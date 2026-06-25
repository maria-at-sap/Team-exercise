import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from models import Document
from word_extractor import WordExtractor


@pytest.fixture
def extractor() -> WordExtractor:
    return WordExtractor()


def test_supports_docx(extractor: WordExtractor) -> None:
    assert extractor.supports(Path("report.docx"))


def test_does_not_support_pdf(extractor: WordExtractor) -> None:
    assert not extractor.supports(Path("report.pdf"))


def test_raises_for_missing_file(extractor: WordExtractor, tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        extractor.extract(tmp_path / "nonexistent.docx")


# TODO: Add a test that creates a real .docx file and checks that:
#   - document.text is not empty
#   - document.title matches the filename stem (or the title in core_properties)
#   - document.word_count() returns a positive integer
#
# Hint: use the `docx` library to create a temporary .docx in `tmp_path`:
#
#   import docx
#   doc = docx.Document()
#   doc.add_paragraph("Hello world")
#   p = tmp_path / "sample.docx"
#   doc.save(p)
#   result = extractor.extract(p)
#   assert "Hello" in result.text
