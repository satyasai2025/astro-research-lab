"""
Astro Research Lab

Dasamsa (D10) Engine
"""

from __future__ import annotations

from copy import deepcopy

from app.engines.divisional.base import (
    DivisionalChartBase,
    SIGNS,
)

from app.engines.models.planet import Planet


class DasamsaEngine(DivisionalChartBase):

    DIVISIONS = 10

    # --------------------------------------------------

    def calculate(
        self,
        planets: dict[str, Planet],
    ) -> dict[str, Planet]:

        d10: dict[str, Planet] = {}

        for name, planet in planets.items():

            p = deepcopy(planet)

            sign = p.sign_index

            dasamsa = self.division_index(
                p.longitude,
                self.DIVISIONS,
            )

            # ------------------------------------------
            # Odd Signs
            # ------------------------------------------

            if self.is_odd_sign(sign):

                new_sign = (

                    sign + dasamsa

                ) % 12

            # ------------------------------------------
            # Even Signs
            # ------------------------------------------

            else:

                new_sign = (

                    sign + 8 + dasamsa

                ) % 12

            division = self.division_size(
                self.DIVISIONS
            )

            degree = (

                self.degree_in_sign(
                    p.longitude
                )

                % division

            ) * self.DIVISIONS

            p.sign_index = new_sign

            p.sign = SIGNS[new_sign]

            p.degree = round(
                degree,
                6,
            )

            d10[name] = p

        return d10


# ------------------------------------------------------

if __name__ == "__main__":

    from datetime import datetime

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

    d10 = DasamsaEngine().calculate(
        planets
    )

    print()

    print("=" * 80)

    print("DASAMSA (D10)")

    print("=" * 80)

    print()

    for planet in d10.values():

        print(

            f"{planet.name:<10}"

            f"{planet.sign:<15}"

            f"{planet.degree:>8.4f}"

        )