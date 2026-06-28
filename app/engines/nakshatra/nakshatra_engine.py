"""
Astro Research Lab

Nakshatra Engine
"""

from __future__ import annotations

from app.engines.models.planet import Planet


NAKSHATRAS = [

    ("Ashwini", "Ketu"),
    ("Bharani", "Venus"),
    ("Krittika", "Sun"),
    ("Rohini", "Moon"),
    ("Mrigashira", "Mars"),
    ("Ardra", "Rahu"),
    ("Punarvasu", "Jupiter"),
    ("Pushya", "Saturn"),
    ("Ashlesha", "Mercury"),
    ("Magha", "Ketu"),
    ("Purva Phalguni", "Venus"),
    ("Uttara Phalguni", "Sun"),
    ("Hasta", "Moon"),
    ("Chitra", "Mars"),
    ("Swati", "Rahu"),
    ("Vishakha", "Jupiter"),
    ("Anuradha", "Saturn"),
    ("Jyeshtha", "Mercury"),
    ("Mula", "Ketu"),
    ("Purva Ashadha", "Venus"),
    ("Uttara Ashadha", "Sun"),
    ("Shravana", "Moon"),
    ("Dhanishta", "Mars"),
    ("Shatabhisha", "Rahu"),
    ("Purva Bhadrapada", "Jupiter"),
    ("Uttara Bhadrapada", "Saturn"),
    ("Revati", "Mercury"),

]


class NakshatraEngine:

    NAKSHATRA_SIZE = 13.3333333333

    PADA_SIZE = 3.3333333333

    # --------------------------------------------------

    def assign(

        self,

        planets: dict[str, Planet],

    ) -> None:

        for planet in planets.values():

            longitude = planet.longitude % 360

            nak_index = int(

                longitude / self.NAKSHATRA_SIZE

            )

            pada = int(

                (longitude % self.NAKSHATRA_SIZE)

                / self.PADA_SIZE

            ) + 1

            nakshatra, lord = NAKSHATRAS[nak_index]

            planet.nakshatra = nakshatra

            planet.pada = pada

            planet.nakshatra_lord = lord