"""
Astro Research Lab

Chart Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from app.engines.models.house import House
from app.engines.models.planet import Planet


@dataclass(slots=True)
class Chart:

    name: str = ""

    birth_date: str = ""

    birth_time: str = ""

    latitude: float = 0.0

    longitude: float = 0.0

    timezone: float = 0.0

    julian_day: float = 0.0

    ayanamsa: float = 0.0

    ascendant_longitude: float = 0.0

    ascendant_sign: str = ""

    ascendant_degree: float = 0.0

    planets: Dict[str, Planet] = field(default_factory=dict)

    houses: List[House] = field(default_factory=list)

    notes: str = ""

    # ----------------------------------------------------

    def add_planet(self, planet: Planet) -> None:

        self.planets[planet.name] = planet

    # ----------------------------------------------------

    def get_planet(self, name: str) -> Planet | None:

        return self.planets.get(name)

    # ----------------------------------------------------

    def add_house(self, house: House) -> None:

        self.houses.append(house)

    # ----------------------------------------------------

    def get_house(self, number: int) -> House:

        if not 1 <= number <= 12:
            raise ValueError("House number must be between 1 and 12.")

        return self.houses[number - 1]

    # ----------------------------------------------------

    def planets_in_house(self, number: int) -> List[Planet]:

        return [

            planet

            for planet in self.planets.values()

            if planet.house == number

        ]

    # ----------------------------------------------------

    def to_dict(self) -> dict:

        return {

            "name": self.name,

            "birth_date": self.birth_date,

            "birth_time": self.birth_time,

            "latitude": self.latitude,

            "longitude": self.longitude,

            "timezone": self.timezone,

            "julian_day": self.julian_day,

            "ayanamsa": self.ayanamsa,

            "ascendant": {

                "longitude": self.ascendant_longitude,

                "sign": self.ascendant_sign,

                "degree": self.ascendant_degree,

            },

            "planets": {

                k: v.to_dict()

                for k, v in self.planets.items()

            },

            "houses": [

                h.to_dict()

                for h in self.houses

            ],

            "notes": self.notes,

        }

    # ----------------------------------------------------

    def summary(self) -> str:

        return (

            f"{self.name} | "

            f"Lagna: {self.ascendant_sign} "

            f"{self.ascendant_degree:.4f}° | "

            f"Planets: {len(self.planets)}"

        )

    # ----------------------------------------------------

    def __str__(self) -> str:

        return self.summary()