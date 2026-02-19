from __future__ import annotations

from app.domain.types import KnightStats


def duel_once(left: KnightStats, right: KnightStats) -> None:
    left_hp_before = left["hp"]
    right_hp_before = right["hp"]

    left["hp"] = left_hp_before - (right["power"] - left["protection"])
    right["hp"] = right_hp_before - (left["power"] - right["protection"])

    if left["hp"] <= 0:
        left["hp"] = 0
    if right["hp"] <= 0:
        right["hp"] = 0
