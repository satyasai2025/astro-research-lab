"""
Astro Research Lab

Chart Populator
"""

from __future__ import annotations

from app.engines.models.chart import Chart


class ChartPopulator:

    def populate(

        self,

        chart: Chart,

        planets: dict,

        houses: list,

        ascendant,

    ) -> Chart:

        chart.ascendant_longitude = ascendant.longitude
        chart.ascendant_sign = ascendant.sign
        chart.ascendant_degree = ascendant.degree

        chart.planets.clear()
        chart.houses.clear()

        for planet in planets.values():
            chart.add_planet(planet)

        for house in houses:
            chart.add_house(house)

        return chart


if __name__ == "__main__":

    from datetime import datetime

    from app.engines.chart_engine.house_assignment import HouseAssignment
    from app.engines.chart_engine.house_calculator import HouseCalculator
    from app.engines.chart_engine.planet_calculator import PlanetCalculator
    from app.engines.chart_engine.sign_assignment import SignAssignment
    from app.engines.models.chart import Chart

    planets = PlanetCalculator().calculate(

        datetime(

            1995,

            8,

            15,

            10,

            30,

        )

    )

    SignAssignment().assign(planets)

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

    chart = Chart()

    ChartPopulator().populate(

        chart,

        planets,

        houses,

        ascendant,

    )

    print()

    print("=" * 80)

    print("CHART SUMMARY")

    print("=" * 80)

    print()

    print(chart)

    print()

    print("Planets :", len(chart.planets))

    print("Houses  :", len(chart.houses))