"""
Astro Research Lab

Sign Assignment Engine
"""

from __future__ import annotations

from app.engines.models.planet import Planet


class SignAssignment:

    EXALTATION = {
        "Sun": "Aries",
        "Moon": "Taurus",
        "Mars": "Capricorn",
        "Mercury": "Virgo",
        "Jupiter": "Cancer",
        "Venus": "Pisces",
        "Saturn": "Libra",
    }

    DEBILITATION = {
        "Sun": "Libra",
        "Moon": "Scorpio",
        "Mars": "Cancer",
        "Mercury": "Pisces",
        "Jupiter": "Capricorn",
        "Venus": "Virgo",
        "Saturn": "Aries",
    }

    OWN_SIGNS = {
        "Sun": {"Leo"},
        "Moon": {"Cancer"},
        "Mars": {"Aries", "Scorpio"},
        "Mercury": {"Gemini", "Virgo"},
        "Jupiter": {"Sagittarius", "Pisces"},
        "Venus": {"Taurus", "Libra"},
        "Saturn": {"Capricorn", "Aquarius"},
    }

    BENEFICS = {
        "Jupiter",
        "Venus",
        "Moon",
    }

    MALEFICS = {
        "Sun",
        "Mars",
        "Saturn",
        "Rahu",
        "Ketu",
    }

    # ---------------------------------------------------------

    def assign(

        self,

        planets: dict[str, Planet],

    ) -> None:

        for planet in planets.values():

            planet.exalted = False
            planet.debilitated = False
            planet.own_sign = False
            planet.is_benefic = False
            planet.is_malefic = False
            planet.dignity = "Neutral"

            if planet.name in self.EXALTATION:

                if planet.sign == self.EXALTATION[planet.name]:

                    planet.exalted = True
                    planet.dignity = "Exalted"

            if planet.name in self.DEBILITATION:

                if planet.sign == self.DEBILITATION[planet.name]:

                    planet.debilitated = True
                    planet.dignity = "Debilitated"

            if planet.name in self.OWN_SIGNS:

                if planet.sign in self.OWN_SIGNS[planet.name]:

                    planet.own_sign = True

                    if planet.dignity == "Neutral":

                        planet.dignity = "Own Sign"

            if planet.name in self.BENEFICS:

                planet.is_benefic = True

            if planet.name in self.MALEFICS:

                planet.is_malefic = True


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

    SignAssignment().assign(

        planets

    )

    print()

    print("=" * 90)

    print("SIGN ASSIGNMENT")

    print("=" * 90)

    print()

    for planet in planets.values():

        print(

            f"{planet.name:<10}"

            f"{planet.sign:<12}"

            f"{planet.dignity:<15}"

            f"Benefic={planet.is_benefic:<5}"

            f"Malefic={planet.is_malefic}"

        )