"""
Astro Research Lab

Conjunction Engine
"""

from __future__ import annotations

from dataclasses import dataclass

from app.engines.models.planet import Planet


@dataclass(slots=True)
class Conjunction:

    planet1: str

    planet2: str

    separation: float

    same_sign: bool

    same_house: bool


class ConjunctionEngine:

    DEFAULT_ORB = 8.0

    # -----------------------------------------------------

    @staticmethod
    def angular_distance(a: float, b: float) -> float:

        diff = abs(a - b)

        return min(diff, 360 - diff)

    # -----------------------------------------------------

    def calculate(

        self,

        planets: dict[str, Planet],

        orb: float | None = None,

    ) -> list[Conjunction]:

        if orb is None:

            orb = self.DEFAULT_ORB

        values = list(planets.values())

        conjunctions = []

        for i in range(len(values)):

            for j in range(i + 1, len(values)):

                p1 = values[i]

                p2 = values[j]

                separation = self.angular_distance(

                    p1.longitude,

                    p2.longitude,

                )

                if separation <= orb:

                    conjunctions.append(

                        Conjunction(

                            planet1=p1.name,

                            planet2=p2.name,

                            separation=round(

                                separation,

                                4,

                            ),

                            same_sign=(

                                p1.sign == p2.sign

                            ),

                            same_house=(

                                p1.bhava_house

                                ==

                                p2.bhava_house

                            ),

                        )

                    )

        return conjunctions


# ---------------------------------------------------------

if __name__ == "__main__":

    from datetime import datetime

    from app.engines.chart_engine.planet_calculator import PlanetCalculator

    planets = PlanetCalculator().calculate(

        datetime(

            1995,

            8,

            15,

            10,

            30,

        )

    )

    conjunctions = ConjunctionEngine().calculate(

        planets

    )

    print()

    print("=" * 80)

    print("CONJUNCTIONS")

    print("=" * 80)

    print()

    for c in conjunctions:

        print(

            f"{c.planet1:<10}"

            f"{c.planet2:<10}"

            f"{c.separation:>8.2f}°"

        )