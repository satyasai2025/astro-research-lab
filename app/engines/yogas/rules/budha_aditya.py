"""
Astro Research Lab

Budha Aditya Yoga
"""

from __future__ import annotations

from app.engines.yogas.base import (
    YogaBase,
    YogaResult,
)


class BudhaAdityaYoga(YogaBase):

    NAME = "Budha Aditya Yoga"

    DESCRIPTION = (
        "Sun and Mercury occupy the same sign."
    )

    def evaluate(self, chart) -> YogaResult:

        sun = chart.planets.get("Sun")

        mercury = chart.planets.get("Mercury")

        if sun is None or mercury is None:

            return YogaResult(

                name=self.NAME,

                present=False,

                description="Sun or Mercury missing.",

            )

        same_sign = (

            sun.sign == mercury.sign

        )

        return YogaResult(

            name=self.NAME,

            present=same_sign,

            strength=1.0 if same_sign else 0.0,

            description=(

                self.DESCRIPTION

                if same_sign

                else "Sun and Mercury are not in the same sign."

            ),

            planets=[

                "Sun",

                "Mercury",

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

    yoga = BudhaAdityaYoga()

    result = yoga.evaluate(chart)

    print()

    print("=" * 70)

    print("BUDHA ADITYA YOGA")

    print("=" * 70)

    print()

    print(f"Present     : {result.present}")

    print(f"Strength    : {result.strength}")

    print(f"Description : {result.description}")

    print(f"Planets     : {', '.join(result.planets)}")