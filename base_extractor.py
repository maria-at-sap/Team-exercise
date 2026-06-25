from abc import ABC, abstractmethod
from pathlib import Path

from models import Document


class DocumentExtractor(ABC):
    """Base class for all document extractors.

    Each subclass must implement `extract` for its specific file format.
    """

    @abstractmethod
    def extract(self, path: Path) -> Document:
        """Read the file at *path* and return a Document.

        Args:
            path: Absolute or relative path to the document file.

        Returns:
            A populated Document instance.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file format is not supported.
        """
        ...

    def supports(self, path: Path) -> bool:
        """Return True if this extractor handles the given file extension."""
        return path.suffix.lower() in self.supported_extensions

    @property
    @abstractmethod
    def supported_extensions(self) -> list[str]:
        """List of lowercase file extensions this extractor handles (e.g. ['.pdf'])."""
        ...
