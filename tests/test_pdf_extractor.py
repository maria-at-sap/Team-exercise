import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from models import Document
from pdf_extractor import PdfExtractor


@pytest.fixture
def extractor() -> PdfExtractor:
    return PdfExtractor()


def test_supports_pdf(extractor: PdfExtractor) -> None:
    assert extractor.supports(Path("report.pdf"))


def test_does_not_support_docx(extractor: PdfExtractor) -> None:
    assert not extractor.supports(Path("report.docx"))


def test_raises_for_missing_file(extractor: PdfExtractor, tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        extractor.extract(tmp_path / "nonexistent.pdf")


# TODO: Add a test that creates a real .pdf file and checks that:
#   - document.text is not empty
#   - document.title matches the filename stem (or the title in metadata)
#   - document.word_count() returns a positive integer
#
# Hint: use the `fpdf2` library to create a minimal PDF in `tmp_path`:
#
#   from fpdf import FPDF
#   pdf = FPDF()
#   pdf.add_page()
#   pdf.set_font("Helvetica", size=12)
#   pdf.cell(text="Hello world")
#   p = tmp_path / "sample.pdf"
#   pdf.output(str(p))
#   result = extractor.extract(p)
#   assert "Hello" in result.text
