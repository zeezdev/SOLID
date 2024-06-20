"""
Data providing low level. Depends on the core's interfaces
"""
from abc import ABC, abstractmethod

from DIP.python.data.decoders import UserDecoder, DeviceDecoder, StatisticsDecoder
from DIP.python.core.models import User, Device, StatisticLog
from DIP.python.core.interfaces import GetUsersInterface, GetDevicesInterface, GetStatisticsInterface


class DataInterface(ABC):

    @abstractmethod
    def get_data(self, data_source: str) -> dict:
        """Retrieve & return data"""


class DataProvider(GetUsersInterface, GetDevicesInterface, GetStatisticsInterface):

    def __init__(self, data_adapter: DataInterface):
        self._data_adapter = data_adapter

    def get_users(self) -> list[User]:
        data = self._data_adapter.get_data(data_source='users')
        decoder = UserDecoder()
        return [decoder.decode(d) for d in data]

    def get_devices(self) -> list[Device]:
        data = self._data_adapter.get_data(data_source='devices')
        decoder = DeviceDecoder()
        return [decoder.decode(d) for d in data]

    def get_statistics(self) -> list[StatisticLog]:
        data = self._data_adapter.get_data(data_source='statistics')
        decoder = StatisticsDecoder()
        return [decoder.decode(d) for d in data]
