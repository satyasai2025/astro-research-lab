"""
Astro Research Lab

Chart Validator
"""

from __future__ import annotations

from app.engines.models.chart import Chart


class ChartValidator:

    REQUIRED_PLANETS = {
        "Sun",
        "Moon",
        "Mars",
        "Mercury",
        "Jupiter",
        "Venus",
        "Saturn",
        "Rahu",
        "Ketu",
    }

    # ---------------------------------------------------------

    def validate(self, chart: Chart) -> None:

        self._validate_planets(chart)

        self._validate_houses(chart)

        self._validate_ascendant(chart)

    # ---------------------------------------------------------

    def _validate_planets(self, chart: Chart) -> None:

        missing = self.REQUIRED_PLANETS - set(chart.planets.keys())

        if missing:

            raise ValueError(

                f"Missing planets: {', '.join(sorted(missing))}"

            )

    # ---------------------------------------------------------

    def _validate_houses(self, chart: Chart) -> None:

        if len(chart.houses) != 12:

            raise ValueError(

                f"Expected 12 houses, got {len(chart.houses)}"

            )

    # ---------------------------------------------------------

    def _validate_ascendant(self, chart: Chart) -> None:

        if not chart.ascendant_sign:

            raise ValueError(

                "Ascendant sign missing."

            )

        if not (0 <= chart.ascendant_degree < 30):

            raise ValueError(

                "Ascendant degree must be between 0° and 30°."

            )


if __name__ == "__main__":

    from datetime import datetime

    from app.engines.chart_engine.chart_populator import ChartPopulator
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

    ChartValidator().validate(chart)

    print()

    print("=" * 70)

    print("✓ CHART VALIDATION SUCCESSFUL")

    print("=" * 70)