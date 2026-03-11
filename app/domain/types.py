from __future__ import annotations

from typing import Any, TypedDict


class ArmourPart(TypedDict):
    part: str
    protection: int


class Weapon(TypedDict):
    name: str
    power: int


class Potion(TypedDict, total=False):
    name: str
    effect: dict[str, int]


class KnightConfig(TypedDict):
    name: str
    power: int
    hp: int
    armour: list[ArmourPart]
    weapon: Weapon
    potion: Potion | None


class KnightStats(TypedDict):
    name: str
    hp: int
    power: int
    protection: int


KnightsConfig = dict[str, KnightConfig]
BattleResult = dict[str, int]
AnyDict = dict[str, Any]
