class Paragraph:
    def __init__(self, content: str):
        self.content = content
        self._char_pointer_idx = 0

    def shift_pointer(self):
        self._char_pointer_idx += 1

    def get_char(self):
        return self.content[self._char_pointer_idx]

    def __str__(self):
        return self.content

    def __repr__(self):
        ptr_idx = self._char_pointer_idx
        at_char = self[self._char_pointer_idx]
        return f"<Paragraph object with char_pointer_idx: {ptr_idx}, pointing at {at_char}>"

    def __getitem__(self, item):
        return self.content[item]

    @property
    def current_idx(self):
        """The index that is currently pointing to a character in the paragraph."""
        return self._char_pointer_idx

    @classmethod
    def clean(cls, content: str):
        content = " ".join(content.splitlines()).strip()
        return cls(content)
