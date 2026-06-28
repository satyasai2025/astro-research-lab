"""
Astro Research Lab

Navamsa (D9) Engine
"""

from __future__ import annotations

from copy import deepcopy

from app.engines.divisional.base import (
    DivisionalChartBase,
    SIGNS,
)
from app.engines.models.planet import Planet


class NavamsaEngine(DivisionalChartBase):

    DIVISIONS = 9

    # --------------------------------------------------

    def calculate(
        self,
        planets: dict[str, Planet],
    ) -> dict[str, Planet]:

        d9_planets: dict[str, Planet] = {}

        for name, planet in planets.items():

            p = deepcopy(planet)

            sign = p.sign_index

            navamsa = self.division_index(
                p.longitude,
                self.DIVISIONS,
            )

            # ------------------------------------------
            # Movable Signs
            # Aries Cancer Libra Capricorn
            # ------------------------------------------

            if self.movable(sign):

                new_sign = (sign + navamsa) % 12

            # ------------------------------------------
            # Fixed Signs
            # Taurus Leo Scorpio Aquarius
            # ------------------------------------------

            elif self.fixed(sign):

                new_sign = (sign + 8 + navamsa) % 12

            # ------------------------------------------
            # Dual Signs
            # Gemini Virgo Sagittarius Pisces
            # ------------------------------------------

            else:

                new_sign = (sign + 4 + navamsa) % 12

            division = self.division_size(
                self.DIVISIONS
            )

            degree = (
                self.degree_in_sign(p.longitude)
                % division
            ) * self.DIVISIONS

            p.sign_index = new_sign

            p.sign = SIGNS[new_sign]

            p.degree = round(degree, 6)

            d9_planets[name] = p

        return d9_planets


# ----------------------------------------------------------

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

    d9 = NavamsaEngine().calculate(planets)

    print()

    print("=" * 80)

    print("NAVAMSA (D9)")

    print("=" * 80)

    for planet in d9.values():

        print(

            f"{planet.name:<10}"

            f"{planet.sign:<15}"

            f"{planet.degree:>8.4f}"

        )