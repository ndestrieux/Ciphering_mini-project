class ChoiceOutOfRange(Exception):
    def __init__(self, choices):
        self.choices = choices
        super().__init__(self.message)

    @property
    def message(self) -> str:
        return f"Choice not in range of {self.choices[0]}-{self.choices[-1]}."
