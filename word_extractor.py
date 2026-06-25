from pathlib import Path

from base_extractor import DocumentExtractor
from models import Document


class WordExtractor(DocumentExtractor):
    """Extracts text and metadata from .docx files."""

    @property
    def supported_extensions(self) -> list[str]:
        return [".docx"]

    def extract(self, path: Path) -> Document:
        """TODO: Implement Word document extraction.

        Suggested library: python-docx
            pip install python-docx

        Steps to implement:
        1. Open the .docx file using `docx.Document(path)`.
        2. Iterate over `doc.paragraphs` to collect all paragraph text.
        3. Join paragraphs into a single string for `Document.text`.
        4. Extract metadata such as the author and last-modified date from
           `doc.core_properties`.
        5. Use the file stem as the title if no title is set in properties.
        6. Return a Document instance.

        Stretch goals:
        - Also extract text from tables (`doc.tables`).
        - Handle embedded images (count them and store the count in metadata).
        """
        raise NotImplementedError
