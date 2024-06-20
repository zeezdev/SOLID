"""
Business logic implementations (depend on the business logic interfaces from core/interfaces.py).
"""

from DIP.python.core.interfaces import GetUsersInterface, GetDevicesInterface, GetStatisticsInterface
from DIP.python.core.models import User, Device, StatisticLog


class UserService:

    def __init__(self, provider: GetUsersInterface):
        self._provider = provider

    def get_active_users(self) -> list[User]:
        users = self._provider.get_users()
        active_users = [u for u in users if u.is_active]
        return active_users

    # TODO: more useful methods


class DeviceService:

    def __init__(self, provider: GetDevicesInterface):
        self._provider = provider

    def get_devices_by_manufacturer(self, manufacturer: str) -> list[Device]:
        devices = self._provider.get_devices()
        selected_devices = [d for d in devices if d.manufacturer == manufacturer]
        return selected_devices

    # TODO: more useful methods


class StatisticsService:

    def __init__(self, provider: GetStatisticsInterface):
        self._provider = provider

    def get_device_statistics_for_users(self, username: str) -> list[StatisticLog]:
        statistics = self._provider.get_statistics()
        user_statistics = [s for s in statistics if s.user_username == username]
        return user_statistics

    # TODO: more useful methods
