from abc import ABC, abstractmethod
from dataclasses import dataclass

from DIP.python.core.models import User, Device, StatisticLog


class DecodableInterface(ABC):

    @abstractmethod
    def decode(self, data: dict) -> dataclass:
        """Decode data into the model instance"""


class UserDecoder(DecodableInterface):

    def decode(self, data: dict) -> User:
        return User(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            is_active=data['is_active'],
        )


class DeviceDecoder(DecodableInterface):

    def decode(self, data: dict) -> Device:
        return Device(
            uid=data['uid'],
            name=data['name'],
            manufacturer=data['manufacturer'],
        )


class StatisticsDecoder(DecodableInterface):

    def decode(self, data: dict) -> StatisticLog:
        return StatisticLog(
            user_username=data['user_username'],
            device_uid=data['device_uid'],
            timestamp=data['timestamp'],
            is_on=data['is_on'],
        )
