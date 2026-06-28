"""
Astro Research Lab

Chandra Mangala Yoga

Moon and Mars are either:
1. In conjunction (same sign), or
2. In mutual 7th aspect.
"""

from __future__ import annotations

from app.engines.yogas.base import (
    YogaBase,
    YogaResult,
)


class ChandraMangalaYoga(YogaBase):

    NAME = "Chandra Mangala Yoga"

    DESCRIPTION = (
        "Moon and Mars are conjoined or mutually aspect each other."
    )

    @staticmethod
    def house_difference(source: int, target: int) -> int:

        return ((target - source) % 12) + 1

    def evaluate(self, chart) -> YogaResult:

        moon = chart.planets.get("Moon")

        mars = chart.planets.get("Mars")

        if moon is None or mars is None:

            return YogaResult(

                name=self.NAME,

                present=False,

                description="Moon or Mars missing.",

            )

        same_sign = moon.sign == mars.sign

        difference = self.house_difference(

            moon.bhava_house,

            mars.bhava_house,

        )

        mutual_aspect = difference == 7

        present = same_sign or mutual_aspect

        return YogaResult(

            name=self.NAME,

            present=present,

            strength=1.0 if present else 0.0,

            description=(

                self.DESCRIPTION

                if present

                else "Moon and Mars neither conjoin nor mutually aspect."

            ),

            planets=[

                "Moon",

                "Mars",

            ],

        )


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

    yoga = ChandraMangalaYoga()

    result = yoga.evaluate(chart)

    print()

    print("=" * 70)

    print("CHANDRA MANGALA YOGA")

    print("=" * 70)

    print()

    print(f"Present     : {result.present}")

    print(f"Strength    : {result.strength}")

    print(f"Description : {result.description}")

    print(f"Planets     : {', '.join(result.planets)}")