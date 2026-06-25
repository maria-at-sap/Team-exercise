from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Document:
    """Represents the extracted content of a single document."""

    source: Path
    title: str
    text: str
    metadata: dict = field(default_factory=dict)

    def word_count(self) -> int:
        return len(self.text.split())
