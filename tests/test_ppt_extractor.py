import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from models import Document
from ppt_extractor import PptExtractor


@pytest.fixture
def extractor() -> PptExtractor:
    return PptExtractor()


def test_supports_pptx(extractor: PptExtractor) -> None:
    assert extractor.supports(Path("slides.pptx"))


def test_does_not_support_pdf(extractor: PptExtractor) -> None:
    assert not extractor.supports(Path("slides.pdf"))


def test_raises_for_missing_file(extractor: PptExtractor, tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        extractor.extract(tmp_path / "nonexistent.pptx")


# TODO: Add a test that creates a real .pptx file and checks that:
#   - document.text is not empty
#   - document.metadata contains the slide count
#   - document.word_count() returns a positive integer
#
# Hint: use the `python-pptx` library to create a minimal presentation:
#
#   from pptx import Presentation
#   from pptx.util import Inches
#   prs = Presentation()
#   slide = prs.slides.add_slide(prs.slide_layouts[5])
#   txBox = slide.shapes.add_textbox(Inches(1), Inches(1), Inches(4), Inches(2))
#   txBox.text_frame.text = "Hello world"
#   p = tmp_path / "sample.pptx"
#   prs.save(str(p))
#   result = extractor.extract(p)
#   assert "Hello" in result.text
