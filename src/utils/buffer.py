from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Buffer:
    encrypted_text_dict: Dict = field(
        default_factory=lambda: {"ROT47": [], "ROT13": []}
    )

    def add(self, key, text):
        self.encrypted_text_dict[key].append(text)

    def clear(self):
        self.encrypted_text_dict = {"ROT47": [], "ROT13": []}

    def __str__(self):
        return str(self.encrypted_text_dict)
