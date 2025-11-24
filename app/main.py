from __future__ import annotations
from abc import ABC


class IntegerRange:
    def __init__(self, min_amount: int, max_amount: int):
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __set_name__(self, owner: type, name: str) -> None:
        self.protected_name = "_" + name

    def __get__(self, instance: object, owner: type) -> object:
        return getattr(instance, self.protected_name)

    def __set__(self, instance: object, value: object) -> None:
        if not isinstance(value, int):
            raise TypeError()
        if not (self.min_amount <= value <= self.max_amount):
            raise ValueError()
        setattr(instance, self.protected_name, value)


class Visitor:
   def __init__(self, name: str, age: int, weight: int, height: int) -> None:
      self.name = name
      self.age = age
      self.weight = weight
      self.height = height


class SlideLimitationValidator(ABC):
    def __init__(self, age: int, weight: int, height: int) -> None:
        self.age = age
        self.weight = weight
        self.height = height


class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    pass


class AdultSlideLimitationValidator(SlideLimitationValidator):
    pass


class Slide:
    pass
