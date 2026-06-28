"""
Astro Research Lab

Chart Builder
Public API
"""

from __future__ import annotations

from datetime import datetime

from app.engines.chart_engine.chart_populator import ChartPopulator
from app.engines.chart_engine.house_assignment import HouseAssignment
from app.engines.chart_engine.house_calculator import HouseCalculator
from app.engines.chart_engine.planet_calculator import PlanetCalculator
from app.engines.chart_engine.sign_assignment import SignAssignment
from app.engines.chart_engine.validator import ChartValidator

from app.engines.models.chart import Chart


class ChartEngine:

    def __init__(self):

        self.planets = PlanetCalculator()

        self.houses = HouseCalculator()

        self.house_assignment = HouseAssignment()

        self.sign_assignment = SignAssignment()

        self.populator = ChartPopulator()

        self.validator = ChartValidator()

    # -----------------------------------------------------

    def build_chart(

        self,

        name: str,

        birth_datetime: datetime,

        latitude: float,

        longitude: float,

        timezone: float = 0.0,

    ) -> Chart:

        chart = Chart()

        chart.name = name

        chart.birth_date = birth_datetime.strftime("%Y-%m-%d")

        chart.birth_time = birth_datetime.strftime("%H:%M:%S")

        chart.latitude = latitude

        chart.longitude = longitude

        chart.timezone = timezone

        planets = self.planets.calculate(

            birth_datetime

        )

        houses, ascendant = self.houses.calculate(

            birth_datetime,

            latitude,

            longitude,

        )

        self.house_assignment.assign(

            planets,

            houses,

        )

        self.sign_assignment.assign(

            planets,

        )

        self.populator.populate(

            chart,

            planets,

            houses,

            ascendant,

        )

        self.validator.validate(

            chart

        )

        return chart

    # -----------------------------------------------------

    def print_chart(

        self,

        chart: Chart,

    ) -> None:

        print()

        print("=" * 90)

        print("ASTRO RESEARCH LAB")

        print("=" * 90)

        print()

        print(

            f"Name      : {chart.name}"

        )

        print(

            f"Lagna     : "

            f"{chart.ascendant_sign} "

            f"{chart.ascendant_degree:.4f}°"

        )

        print()

        print(

            f"{'Planet':<12}"

            f"{'Sign':<14}"

            f"{'House':<8}"

            f"{'Dignity':<15}"

        )

        print("-" * 90)

        for planet in chart.planets.values():

            print(

                f"{planet.name:<12}"

                f"{planet.sign:<14}"

                f"{planet.house:<8}"

                f"{planet.dignity:<15}"

            )

        print()

        print("=" * 90)


if __name__ == "__main__":

    engine = ChartEngine()

    chart = engine.build_chart(

        name="Demo Horoscope",

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

    engine.print_chart(chart)