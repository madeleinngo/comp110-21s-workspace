"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730272774"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        self.values = values

    def __repr__(self) -> str:
        return f"Simpy({self.values})"

    def fill(self, fill: float, number: int) -> None:
        if len(self.values) < number:
            for item in self.values:
                self.values = fill

        return self.values 
