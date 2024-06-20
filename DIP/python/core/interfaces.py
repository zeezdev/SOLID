from abc import ABC, abstractmethod

from DIP.python.core.models import User, Device, StatisticLog


class GetUsersInterface(ABC):

    @abstractmethod
    def get_users(self) -> list[User]:
        """Returns all users"""


class GetDevicesInterface(ABC):

    @abstractmethod
    def get_devices(self) -> list[Device]:
        """Returns all devices"""


class GetStatisticsInterface(ABC):

    @abstractmethod
    def get_statistics(self) -> list[StatisticLog]:
        """Returns all statistics"""
