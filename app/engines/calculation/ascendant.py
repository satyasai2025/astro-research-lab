"""
Astro Research Lab

Ascendant Calculation Engine
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import swisseph as swe


SIGNS = (
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
)


@dataclass(slots=True)
class Ascendant:

    longitude: float

    sign: str

    sign_index: int

    degree: float


class AscendantEngine:

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
    def normalize(value: float) -> float:

        value %= 360.0

        if value < 0:

            value += 360.0

        return value

    # -----------------------------------------------------

    @staticmethod
    def sign_details(longitude: float):

        longitude %= 360

        sign_index = int(longitude // 30)

        degree = longitude % 30

        sign = SIGNS[sign_index]

        return sign, sign_index, degree

    # -----------------------------------------------------

    def calculate(

        self,

        dt: datetime,

        latitude: float,

        longitude: float,

    ) -> Ascendant:

        jd = self.julian_day(dt)

        flags = swe.FLG_SWIEPH | swe.FLG_SIDEREAL

        cusps, ascmc = swe.houses_ex(

            jd,

            latitude,

            longitude,

            b"P",

            flags,

        )

        asc = self.normalize(ascmc[0])

        sign, sign_index, degree = self.sign_details(asc)

        return Ascendant(

            longitude=round(asc, 6),

            sign=sign,

            sign_index=sign_index,

            degree=round(degree, 6),

        )


if __name__ == "__main__":

    engine = AscendantEngine()

    asc = engine.calculate(

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

    print()

    print("=" * 60)

    print("ASCENDANT")

    print("=" * 60)

    print(f"Longitude : {asc.longitude}")

    print(f"Sign      : {asc.sign}")

    print(f"Degree    : {asc.degree}")