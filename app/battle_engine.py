from __future__ import annotations

from copy import deepcopy
from typing import TypedDict


class ArmourConfig(TypedDict):
    part: str
    protection: int


class WeaponConfig(TypedDict):
    name: str
    power: int


class PotionEffect(TypedDict, total=False):
    hp: int
    power: int
    protection: int


class PotionConfig(TypedDict):
    name: str
    effect: PotionEffect


class KnightConfig(TypedDict):
    name: str
    power: int
    hp: int
    armour: list[ArmourConfig]
    weapon: WeaponConfig
    potion: PotionConfig | None


class BattleKnight(TypedDict):
    name: str
    hp: int
    power: int
    protection: int


def battle(knights_config: dict[str, KnightConfig]) -> dict[str, int]:
    prepared_knights = {
        knight_key: prepare_knight(knight_config)
        for knight_key, knight_config in deepcopy(knights_config).items()
    }

    resolve_duel(prepared_knights["lancelot"], prepared_knights["mordred"])
    resolve_duel(prepared_knights["arthur"], prepared_knights["red_knight"])

    return {
        knight["name"]: knight["hp"]
        for knight in prepared_knights.values()
    }


def prepare_knight(knight_config: KnightConfig) -> BattleKnight:
    battle_knight: BattleKnight = {
        "name": knight_config["name"],
        "hp": knight_config["hp"],
        "power": knight_config["power"] + knight_config["weapon"]["power"],
        "protection": get_armour_protection(knight_config["armour"]),
    }
    apply_potion_effects(battle_knight, knight_config["potion"])
    return battle_knight


def get_armour_protection(armour_parts: list[ArmourConfig]) -> int:
    protection = 0

    for armour_part in armour_parts:
        protection += armour_part["protection"]

    return protection


def apply_potion_effects(
    knight: BattleKnight,
    potion: PotionConfig | None,
) -> None:
    if potion is None:
        return

    for stat_name, stat_value in potion["effect"].items():
        knight[stat_name] += stat_value


def resolve_duel(first_knight: BattleKnight, second_knight: BattleKnight) -> None:
    first_damage = max(second_knight["power"] - first_knight["protection"], 0)
    second_damage = max(first_knight["power"] - second_knight["protection"], 0)

    first_knight["hp"] = max(first_knight["hp"] - first_damage, 0)
    second_knight["hp"] = max(second_knight["hp"] - second_damage, 0)
