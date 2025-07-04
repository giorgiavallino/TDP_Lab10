from dataclasses import dataclass

@dataclass
class Country:
    StateAbb: str
    CCode: int
    StateNme: str

    def __hash__(self):
        return hash(self.CCode)

    def __eq__(self, other):
        if isinstance(other, Country):
            return self.CCode == other.CCode
        return False

    def __str__(self):
        return f"{self.StateNme} ({self.StateAbb}, {self.CCode})"