"""
Astro Research Lab

Bhava Chalit Engine
"""

from __future__ import annotations

from app.engines.models.house import House
from app.engines.models.planet import Planet


class BhavaChalitEngine:

    @staticmethod
    def normalize(value: float) -> float:

        value %= 360.0

        if value < 0:
            value += 360.0

        return value

    # --------------------------------------------------------

    def assign(

        self,

        planets: dict[str, Planet],

        houses: list[House],

    ) -> None:

        cusps = [

            self.normalize(

                h.longitude

            )

            for h in houses

        ]

        extended = cusps + [

            cusps[0] + 360.0

        ]

        for planet in planets.values():

            lon = self.normalize(

                planet.longitude

            )

            test = lon

            if test < cusps[0]:

                test += 360.0

            bhava = 12

            for i in range(12):

                if (

                    extended[i]

                    <= test

                    < extended[i + 1]

                ):

                    bhava = i + 1

                    break

            planet.bhava_house = bhava