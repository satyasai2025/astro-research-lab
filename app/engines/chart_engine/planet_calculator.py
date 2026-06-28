"""
Astro Research Lab

Planet Calculator

Wrapper around PlanetPositionEngine.
"""

from __future__ import annotations

from datetime import datetime

from app.engines.calculation.planet_positions import (
    PlanetPositionEngine,
)

from app.engines.models.planet import Planet


class PlanetCalculator:

    def __init__(self):

        self.engine = PlanetPositionEngine()

    # ---------------------------------------------------------

    def calculate(

        self,

        birth_datetime: datetime,

    ) -> dict[str, Planet]:

        raw_planets = self.engine.calculate(

            birth_datetime

        )

        planets: dict[str, Planet] = {}

        for name, p in raw_planets.items():

            planets[name] = Planet(

                name=p.name,

                longitude=p.longitude,

                latitude=0.0,

                speed=0.0,

                sign=p.sign,

                sign_index=p.sign_index,

                degree=p.degree,

                retrograde=p.retrograde,

            )

        return planets


if __name__ == "__main__":

    from datetime import datetime

    calculator = PlanetCalculator()

    planets = calculator.calculate(

        datetime(

            1995,

            8,

            15,

            10,

            30,

        )

    )

    print()

    print("=" * 70)

    print("PLANET CALCULATOR")

    print("=" * 70)

    print()

    for planet in planets.values():

        print(

            f"{planet.name:<10}"

            f"{planet.sign:<12}"

            f"{planet.degree:>8.4f}"

        )