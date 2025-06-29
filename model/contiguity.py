from dataclasses import dataclass

@dataclass
class Contiguity:
    dyad: int
    state1no: int
    state1ab: str
    state2no: int
    state2ab: str
    year: int
    conttype: int
    version: float

    def __hash__(self):
        return hash(self.state1no) and hash(self.state2no)

    def __eq__(self, other):
        if not isinstance(other, Contiguity):
            return False
        return self.state1no == other.state1no and self.state2no == other.state2no

    def __str__(self):
        return f"{self.state1no} - {self.state2no}"