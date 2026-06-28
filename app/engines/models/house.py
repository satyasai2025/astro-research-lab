from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class House:

    number: int

    longitude: float

    sign: str

    sign_index: int

    degree: float

    ruler: str = ""

    occupants: list[str] = field(default_factory=list)

    is_kendra: bool = False

    is_trikona: bool = False

    is_upachaya: bool = False

    is_dusthana: bool = False

    def add_planet(self, planet: str) -> None:

        if planet not in self.occupants:
            self.occupants.append(planet)

    @property
    def planet_count(self) -> int:

        return len(self.occupants)