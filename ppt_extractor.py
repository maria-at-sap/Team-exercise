from pathlib import Path

from base_extractor import DocumentExtractor
from models import Document


class PptExtractor(DocumentExtractor):
    """Extracts text and metadata from .pptx files."""

    @property
    def supported_extensions(self) -> list[str]:
        return [".pptx"]

    def extract(self, path: Path) -> Document:
        """TODO: Implement PowerPoint extraction.

        Suggested library: python-pptx
            pip install python-pptx

        Steps to implement:
        1. Open the file with `pptx.Presentation(path)`.
        2. Iterate over `prs.slides`, then over each slide's `shapes`.
        3. For each shape that `has_text_frame`, iterate its `paragraphs` and `runs`
           to collect all visible text.
        4. Join all collected text into a single string for `Document.text`.
        5. Read metadata from `prs.core_properties` (author, title, etc.).
        6. Store the slide count in metadata.
        7. Return a Document instance.

        Stretch goals:
        - Extract speaker notes from `slide.notes_slide.notes_text_frame`.
        - Record per-slide word counts in metadata.
        """
        raise NotImplementedError
