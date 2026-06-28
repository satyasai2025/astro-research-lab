"""
Astro Research Lab

House Calculator

Combines:
- Ascendant Engine
- House Engine
"""

from __future__ import annotations

from datetime import datetime

from app.engines.calculation.ascendant import (
    AscendantEngine,
)

from app.engines.calculation.houses import (
    HouseEngine,
)

from app.engines.models.house import House


class HouseCalculator:

    def __init__(self):

        self.ascendant_engine = AscendantEngine()

        self.house_engine = HouseEngine()

    # ---------------------------------------------------------

    def calculate(

        self,

        birth_datetime: datetime,

        latitude: float,

        longitude: float,

    ) -> tuple[list[House], object]:

        ascendant = self.ascendant_engine.calculate(

            birth_datetime,

            latitude,

            longitude,

        )

        raw_houses = self.house_engine.calculate(

            birth_datetime,

            latitude,

            longitude,

        )

        houses: list[House] = []

        for h in raw_houses:

            house = House(

                number=h.number,

                longitude=h.longitude,

                sign=h.sign,

                sign_index=h.sign_index,

                degree=h.degree,

            )

            house.is_kendra = h.number in (1, 4, 7, 10)

            house.is_trikona = h.number in (1, 5, 9)

            house.is_upachaya = h.number in (3, 6, 10, 11)

            house.is_dusthana = h.number in (6, 8, 12)

            houses.append(house)

        return houses, ascendant


if __name__ == "__main__":

    calculator = HouseCalculator()

    houses, ascendant = calculator.calculate(

        birth_datetime=datetime(

            1995,

            8,

            15,

            10,

            30,

        ),

        latitude=28.6139,

        longitude=77.2090,

    )

    print()

    print("=" * 70)

    print("ASCENDANT")

    print("=" * 70)

    print(

        ascendant.sign,

        f"{ascendant.degree:.4f}°",

    )

    print()

    print("=" * 70)

    print("HOUSES")

    print("=" * 70)

    for house in houses:

        print(

            f"{house.number:>2} "

            f"{house.sign:<12}"

            f"{house.degree:>8.4f}"

        )