"""
Astro Research Lab

House Assignment Engine
"""

from __future__ import annotations

from app.engines.models.house import House
from app.engines.models.planet import Planet


class HouseAssignment:

    # ---------------------------------------------------------

    @staticmethod
    def normalize(value: float) -> float:

        value %= 360.0

        if value < 0:
            value += 360.0

        return value

    # ---------------------------------------------------------

    def assign(

        self,

        planets: dict[str, Planet],

        houses: list[House],

    ) -> None:

        # Clear previous occupants
        for house in houses:
            house.occupants.clear()

        # House cusp longitudes
        cusps = [self.normalize(h.longitude) for h in houses]

        # Close the circle
        extended = cusps + [cusps[0] + 360.0]

        # Assign each planet
        for planet in planets.values():

            longitude = self.normalize(planet.longitude)

            test_longitude = longitude

            if test_longitude < cusps[0]:
                test_longitude += 360.0

            assigned_house = 12

            for index in range(12):

                start = extended[index]
                end = extended[index + 1]

                if start <= test_longitude < end:
                    assigned_house = index + 1
                    break

            planet.house = assigned_house

            houses[assigned_house - 1].add_planet(
                planet.name
            )


if __name__ == "__main__":

    from datetime import datetime

    from app.engines.chart_engine.house_calculator import (
        HouseCalculator,
    )

    from app.engines.chart_engine.planet_calculator import (
        PlanetCalculator,
    )

    planets = PlanetCalculator().calculate(

        datetime(

            1995,

            8,

            15,

            10,

            30,

        )

    )

    houses, ascendant = HouseCalculator().calculate(

        datetime(

            1995,

            8,

            15,

            10,

            30,

        ),

        latitude=28.6139,

        longitude=77.2090,

    )

    HouseAssignment().assign(

        planets,

        houses,

    )

    print()

    print("=" * 80)

    print("HOUSE ASSIGNMENT")

    print("=" * 80)

    for house in houses:

        print(

            f"House {house.number:>2} "

            f"{house.sign:<12} "

            f"{house.occupants}"

        )

    print()

    print("=" * 80)

    print("PLANET → HOUSE")

    print("=" * 80)

    for planet in planets.values():

        print(

            f"{planet.name:<10}"

            f"House {planet.house}"

        )