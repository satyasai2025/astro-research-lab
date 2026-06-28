"""
Astro Research Lab

Swiss Ephemeris
Planet Position Engine
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict

import swisseph as swe


# ---------------------------------------------------------
# Constants
# ---------------------------------------------------------

PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mars": swe.MARS,
    "Mercury": swe.MERCURY,
    "Jupiter": swe.JUPITER,
    "Venus": swe.VENUS,
    "Saturn": swe.SATURN,
    "Rahu": swe.MEAN_NODE,
}


SIGNS = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces",
]


# ---------------------------------------------------------
# Models
# ---------------------------------------------------------

@dataclass(slots=True)
class PlanetPosition:

    name: str
    longitude: float
    sign: str
    sign_index: int
    degree: float
    retrograde: bool


# ---------------------------------------------------------
# Engine
# ---------------------------------------------------------

class PlanetPositionEngine:

    def __init__(self):

        swe.set_sid_mode(swe.SIDM_LAHIRI)

    # -----------------------------------------------------

    @staticmethod
    def julian_day(
        dt: datetime,
    ) -> float:

        hour = (
            dt.hour
            + dt.minute / 60
            + dt.second / 3600
        )

        return swe.julday(
            dt.year,
            dt.month,
            dt.day,
            hour,
        )

    # -----------------------------------------------------

    @staticmethod
    def normalize(
        longitude: float,
    ) -> float:

        longitude %= 360.0

        if longitude < 0:
            longitude += 360.0

        return longitude

    # -----------------------------------------------------

    @staticmethod
    def sign_details(
        longitude: float,
    ):

        longitude = longitude % 360

        sign_index = int(longitude // 30)

        sign = SIGNS[sign_index]

        degree = longitude % 30

        return sign, sign_index, degree

    # -----------------------------------------------------

    def calculate(
        self,
        dt: datetime,
    ) -> Dict[str, PlanetPosition]:

        jd = self.julian_day(dt)

        result: Dict[str, PlanetPosition] = {}

        flags = swe.FLG_SWIEPH | swe.FLG_SIDEREAL

        for planet_name, planet_id in PLANETS.items():

            values, _ = swe.calc_ut(
                jd,
                planet_id,
                flags,
            )

            longitude = self.normalize(values[0])

            sign, sign_index, degree = self.sign_details(
                longitude
            )

            result[planet_name] = PlanetPosition(
                name=planet_name,
                longitude=round(longitude, 6),
                sign=sign,
                sign_index=sign_index,
                degree=round(degree, 6),
                retrograde=values[3] < 0,
            )

        # ---------------------------------------------
        # Ketu (180° opposite Rahu)
        # ---------------------------------------------

        rahu = result["Rahu"]

        ketu_longitude = self.normalize(
            rahu.longitude + 180.0
        )

        sign, sign_index, degree = self.sign_details(
            ketu_longitude
        )

        result["Ketu"] = PlanetPosition(
            name="Ketu",
            longitude=round(ketu_longitude, 6),
            sign=sign,
            sign_index=sign_index,
            degree=round(degree, 6),
            retrograde=rahu.retrograde,
        )

        return result


# ---------------------------------------------------------
# Manual Test
# ---------------------------------------------------------

if __name__ == "__main__":

    engine = PlanetPositionEngine()

    positions = engine.calculate(

        datetime(
            1995,
            8,
            15,
            10,
            30,
        )

    )

    print()

    print("=" * 75)

    print("PLANET POSITIONS")

    print("=" * 75)

    for planet in positions.values():

        print(

            f"{planet.name:<10}"

            f"{planet.longitude:>10.4f}°   "

            f"{planet.sign:<12}"

            f"{planet.degree:>8.4f}°   "

            f"Retrograde : {planet.retrograde}"

        )