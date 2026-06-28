"""
Astro Research Lab

Gaja Kesari Yoga

Classical Definition (Version 1)

Moon and Jupiter are placed in Kendras
(1st, 4th, 7th, or 10th) from each other.

Version 2 (Future)
------------------
- Moon not debilitated
- Jupiter not combust
- Benefic/Malefic influences
- Shadbala weighting
- Paksha Bala
"""

from __future__ import annotations

from app.engines.yogas.base import (
    YogaBase,
    YogaResult,
)


class GajaKesariYoga(YogaBase):

    NAME = "Gaja Kesari Yoga"

    DESCRIPTION = (
        "Moon and Jupiter occupy Kendras from each other."
    )

    KENDRAS = (1, 4, 7, 10)

    # --------------------------------------------------------

    @staticmethod
    def house_difference(
        source: int,
        target: int,
    ) -> int:

        return ((target - source) % 12) + 1

    # --------------------------------------------------------

    def evaluate(
        self,
        chart,
    ) -> YogaResult:

        moon = chart.planets.get("Moon")

        jupiter = chart.planets.get("Jupiter")

        if moon is None or jupiter is None:

            return YogaResult(

                name=self.NAME,

                present=False,

                description="Moon or Jupiter missing.",

            )

        difference = self.house_difference(

            moon.bhava_house,

            jupiter.bhava_house,

        )

        present = difference in self.KENDRAS

        return YogaResult(

            name=self.NAME,

            present=present,

            strength=1.0 if present else 0.0,

            description=(

                self.DESCRIPTION

                if present

                else "Moon and Jupiter are not in Kendra."

            ),

            planets=[

                "Moon",

                "Jupiter",

            ],

        )


# ----------------------------------------------------------------------

if __name__ == "__main__":

    from datetime import datetime

    from app.engines.chart_engine.builder import ChartEngine

    chart = ChartEngine().build_chart(

        name="Demo",

        birth_datetime=datetime(

            1995,

            8,

            15,

            10,

            30,

        ),

        latitude=28.6139,

        longitude=77.2090,

        timezone=5.5,

    )

    yoga = GajaKesariYoga()

    result = yoga.evaluate(chart)

    print()

    print("=" * 70)

    print("GAJA KESARI YOGA")

    print("=" * 70)

    print()

    print(f"Present     : {result.present}")

    print(f"Strength    : {result.strength}")

    print(f"Description : {result.description}")

    print(f"Planets     : {', '.join(result.planets)}")