"""
Astro Research Lab

Base Yoga Classes
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass(slots=True)
class YogaResult:

    name: str

    present: bool

    strength: float = 0.0

    description: str = ""

    planets: list[str] = field(default_factory=list)


class YogaBase(ABC):

    NAME = "Unnamed Yoga"

    DESCRIPTION = ""

    @abstractmethod
    def evaluate(self, chart) -> YogaResult:
        """
        Evaluate the yoga.
        """
        raise NotImplementedError