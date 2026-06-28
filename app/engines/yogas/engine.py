"""
Astro Research Lab

Yoga Engine
"""

from __future__ import annotations

from app.engines.yogas.base import YogaBase, YogaResult

from app.engines.yogas.rules import (
    BudhaAdityaYoga,
    GajaKesariYoga,
    ChandraMangalaYoga,
)


class YogaEngine:

    def __init__(self):

        self._yogas: list[YogaBase] = [

            BudhaAdityaYoga(),

            GajaKesariYoga(),
            
            ChandraMangalaYoga(),

        ]

    # ------------------------------------------------------

    def register(

        self,

        yoga: YogaBase,

    ) -> None:

        self._yogas.append(yoga)

    # ------------------------------------------------------

    def evaluate(

        self,

        chart,

    ) -> list[YogaResult]:

        results = []

        for yoga in self._yogas:

            results.append(

                yoga.evaluate(chart)

            )

        return results


# ------------------------------------------------------------

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

    engine = YogaEngine()

    print()

    print("=" * 80)

    print("YOGA ENGINE")

    print("=" * 80)

    print()

    for result in engine.evaluate(chart):

        print(

            f"{result.name:<30}"

            f"{'YES' if result.present else 'NO'}"

        )
        