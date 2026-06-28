"""
Astro Research Lab

Planet Model
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Planet:

    name: str

    longitude: float

    latitude: float

    speed: float

    sign: str

    sign_index: int

    degree: float

    retrograde: bool

    # -------- Position --------

    house: int = 0

    rasi_house: int = 0

    bhava_house: int = 0

    # -------- Zodiac --------

# -------- Zodiac --------

    sign_lord: str = ""

    nakshatra_lord: str = ""

    nakshatra: str = ""

    pada: int = 0

    # -------- Strength --------

    dignity: str = ""

    combust: bool = False

    exalted: bool = False

    debilitated: bool = False

    own_sign: bool = False

    moolatrikona: bool = False

    is_benefic: bool = False

    is_malefic: bool = False

    def to_dict(self) -> dict:

        return {

            "name": self.name,

            "longitude": self.longitude,

            "latitude": self.latitude,

            "speed": self.speed,

            "sign": self.sign,

            "sign_index": self.sign_index,

            "degree": self.degree,

            "retrograde": self.retrograde,

            "house": self.house,

            "rasi_house": self.rasi_house,

            "bhava_house": self.bhava_house,

            "sign_lord": self.sign_lord,
            "nakshatra_lord": self.nakshatra_lord,

            "nakshatra": self.nakshatra,

            "pada": self.pada,

            "dignity": self.dignity,

            "combust": self.combust,

            "exalted": self.exalted,

            "debilitated": self.debilitated,

            "own_sign": self.own_sign,

            "moolatrikona": self.moolatrikona,

            "benefic": self.is_benefic,

            "malefic": self.is_malefic,

        }

    def __str__(self):

        return (

            f"{self.name} "

            f"{self.sign} "

            f"{self.degree:.4f}°"

        )