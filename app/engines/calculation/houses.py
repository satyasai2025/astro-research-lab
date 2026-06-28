"""
Astro Research Lab

House Calculation Engine
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
class House:

    number: int

    longitude: float

    sign: str

    sign_index: int

    degree: float


class HouseEngine:

    def __init__(self):

        swe.set_sid_mode(swe.SIDM_LAHIRI)

    # --------------------------------------------------

    @staticmethod
    def julian_day(dt: datetime):

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

    # --------------------------------------------------

    @staticmethod
    def normalize(value):

        value %= 360.0

        if value < 0:
            value += 360.0

        return value

    # --------------------------------------------------

    @staticmethod
    def sign_details(longitude):

        sign_index = int(longitude // 30)

        sign = SIGNS[sign_index]

        degree = longitude % 30

        return sign, sign_index, degree

    # --------------------------------------------------

    def calculate(

        self,

        dt: datetime,

        latitude: float,

        longitude: float,

    ):

        jd = self.julian_day(dt)

        flags = swe.FLG_SWIEPH | swe.FLG_SIDEREAL

        cusps, ascmc = swe.houses_ex(

            jd,

            latitude,

            longitude,

            b"P",

            flags,

        )

        houses = []

        for i in range(12):

            lon = self.normalize(cusps[i])

            sign, sign_index, degree = self.sign_details(
                lon
            )

            houses.append(

                House(

                    number=i + 1,

                    longitude=round(lon, 6),

                    sign=sign,

                    sign_index=sign_index,

                    degree=round(degree, 6),

                )

            )

        return houses


if __name__ == "__main__":

    engine = HouseEngine()

    houses = engine.calculate(

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

    print("=" * 75)

    print("HOUSE CUSPS")

    print("=" * 75)

    for house in houses:

        print(

            f"House {house.number:>2}   "

            f"{house.longitude:>9.4f}°   "

            f"{house.sign:<12}   "

            f"{house.degree:>7.4f}°"

        )