"""
Models (Data interfaces of the business logic).
"""

from dataclasses import dataclass


@dataclass
class User:
    username: str
    first_name: str
    last_name: str
    is_active: bool


@dataclass
class Device:
    uid: str
    manufacturer: str
    name: str


@dataclass
class StatisticLog:
    user_username: str
    device_uid: str
    timestamp: int
    is_on: bool
