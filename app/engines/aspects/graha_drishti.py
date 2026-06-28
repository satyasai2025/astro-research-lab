"""
Astro Research Lab

Graha Drishti Engine
"""

from __future__ import annotations

from dataclasses import dataclass

from app.engines.models.planet import Planet


@dataclass(slots=True)
class Aspect:

    source: str

    target: str

    aspect: int

    exact: bool


class GrahaDrishtiEngine:

    ASPECTS = {

        "Sun": [7],

        "Moon": [7],

        "Mercury": [7],

        "Venus": [7],

        "Mars": [4, 7, 8],

        "Jupiter": [5, 7, 9],

        "Saturn": [3, 7, 10],

        "Rahu": [5, 7, 9],

        "Ketu": [5, 7, 9],

    }

    # ----------------------------------------------------

    @staticmethod
    def house_difference(

        source: int,

        target: int,

    ) -> int:

        return ((target - source) % 12) + 1

    # ----------------------------------------------------

    def calculate(

        self,

        planets: dict[str, Planet],

    ) -> list[Aspect]:

        aspects: list[Aspect] = []

        values = list(planets.values())

        for source in values:

            source_house = source.bhava_house

            allowed = self.ASPECTS.get(

                source.name,

                [],

            )

            for target in values:

                if source.name == target.name:

                    continue

                difference = self.house_difference(

                    source_house,

                    target.bhava_house,

                )

                if difference in allowed:

                    aspects.append(

                        Aspect(

                            source=source.name,

                            target=target.name,

                            aspect=difference,

                            exact=True,

                        )

                    )

        return aspects


# ----------------------------------------------------------

if __name__ == "__main__":

    from datetime import datetime

    from app.engines.chart_engine.planet_calculator import PlanetCalculator

    from app.engines.chart_engine.house_calculator import HouseCalculator

    from app.engines.chart_engine.house_assignment import HouseAssignment

    from app.engines.bhava.bhava_chalit import BhavaChalitEngine

    planets = PlanetCalculator().calculate(

        datetime(

            1995,

            8,

            15,

            10,

            30,

        )

    )

    houses, asc = HouseCalculator().calculate(

        datetime(

            1995,

            8,

            15,

            10,

            30,

        ),

        28.6139,

        77.2090,

    )

    HouseAssignment().assign(

        planets,

        houses,

    )

    BhavaChalitEngine().assign(

        planets,

        houses,

    )

    aspects = GrahaDrishtiEngine().calculate(

        planets

    )

    print()

    print("=" * 80)

    print("GRAHA DRISHTI")

    print("=" * 80)

    print()

    for aspect in aspects:

        print(

            f"{aspect.source:<10}"

            f"→ "

            f"{aspect.target:<10}"

            f" House {aspect.aspect}"

        )