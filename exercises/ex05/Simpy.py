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
        result: list[float] = []
        while len(result) < number:
            result.append(fill)
        self.values = result

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        result: list[float] = []
        assert step != 0.0
        if step < 0:
            while start > stop:
                result.append(start)
                start += step
        elif step > 0:
            while start < stop:
                result.append(start)
                start += step
        self.values = result

    def sum(self) -> float: 
        result: float
        result = sum(self.values)
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        result: list[float] = []
        if isinstance(rhs, float):
            result: list[float] = []
            for item in self.values:
                result.append(item + rhs) 
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        result: list[float] = []
        if isinstance(rhs, float):
            result: list[float] = []
            for item in self.values:
                result.append(item ** rhs) 
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        return Simpy(result)

    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        result: list[float] = []
        if isinstance(rhs, float):
            result: list[float] = []
            for item in self.values:
                result.append(item % rhs) 
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] % rhs.values[i])
        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs) 
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs) 
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        result: list[float] = []
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            for i in range(len(rhs)):
                if rhs[i]:
                    result.append(self[i])
            return Simpy(result)
