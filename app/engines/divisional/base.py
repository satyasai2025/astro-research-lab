"""
Astro Research Lab

Divisional Chart Base Engine

Shared mathematical utilities for all Vargas.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.engines.models.planet import Planet


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


class DivisionalChartBase(ABC):

    SIGN_SIZE = 30.0

    # --------------------------------------------------

    @staticmethod
    def normalize(longitude: float) -> float:

        longitude %= 360.0

        if longitude < 0:
            longitude += 360.0

        return longitude

    # --------------------------------------------------

    @classmethod
    def sign_index(cls, longitude: float) -> int:

        longitude = cls.normalize(longitude)

        return int(longitude // cls.SIGN_SIZE)

    # --------------------------------------------------

    @classmethod
    def sign_name(cls, longitude: float) -> str:

        return SIGNS[cls.sign_index(longitude)]

    # --------------------------------------------------

    @classmethod
    def degree_in_sign(cls, longitude: float) -> float:

        longitude = cls.normalize(longitude)

        return longitude % cls.SIGN_SIZE

    # --------------------------------------------------

    @classmethod
    def division_size(cls, divisions: int) -> float:

        return cls.SIGN_SIZE / divisions

    # --------------------------------------------------

    @classmethod
    def division_index(

        cls,

        longitude: float,

        divisions: int,

    ) -> int:

        degree = cls.degree_in_sign(longitude)

        return int(

            degree // cls.division_size(divisions)

        )

    # --------------------------------------------------

    @classmethod
    def is_odd_sign(

        cls,

        sign_index: int,

    ) -> bool:

        return sign_index % 2 == 0

    # --------------------------------------------------

    @classmethod
    def is_even_sign(

        cls,

        sign_index: int,

    ) -> bool:

        return not cls.is_odd_sign(sign_index)

    # --------------------------------------------------

    @classmethod
    def movable(

        cls,

        sign_index: int,

    ) -> bool:

        return sign_index in (0, 3, 6, 9)

    # --------------------------------------------------

    @classmethod
    def fixed(

        cls,

        sign_index: int,

    ) -> bool:

        return sign_index in (1, 4, 7, 10)

    # --------------------------------------------------

    @classmethod
    def dual(

        cls,

        sign_index: int,

    ) -> bool:

        return sign_index in (2, 5, 8, 11)

    # --------------------------------------------------

    @abstractmethod
    def calculate(

        self,

        planets: dict[str, Planet],

    ) -> dict[str, Planet]:

        """
        Return planets positioned in this divisional chart.
        """
        raise NotImplementedError