"""
Astro Research Lab

Sign Lord Engine
"""

from __future__ import annotations

from app.engines.models.planet import Planet


SIGN_LORDS = {

    "Aries": "Mars",

    "Taurus": "Venus",

    "Gemini": "Mercury",

    "Cancer": "Moon",

    "Leo": "Sun",

    "Virgo": "Mercury",

    "Libra": "Venus",

    "Scorpio": "Mars",

    "Sagittarius": "Jupiter",

    "Capricorn": "Saturn",

    "Aquarius": "Saturn",

    "Pisces": "Jupiter",

}


class SignLordEngine:

    def assign(

        self,

        planets: dict[str, Planet],

    ) -> None:

        for planet in planets.values():

            planet.sign_lord = SIGN_LORDS.get(

                planet.sign,

                "",

            )


if __name__ == "__main__":

    from datetime import datetime

    from app.engines.chart_engine.planet_calculator import PlanetCalculator

    planets = PlanetCalculator().calculate(

        datetime(

            1995,

            8,

            15,

            10,

            30,

        )

    )

    SignLordEngine().assign(

        planets

    )

    print()

    print("=" * 70)

    print("SIGN LORDS")

    print("=" * 70)

    for planet in planets.values():

        print(

            f"{planet.name:<10}"

            f"{planet.sign:<14}"

            f"{planet.sign_lord}"

        )