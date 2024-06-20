from typing import Any

from DIP.python.data.mocked_data import USERS_DATA, DEVICES_DATA, STATISTICS_DATA
from DIP.python.data.providers import DataInterface


class DataFileAdapter(DataInterface):
    """Imitate data retrieve from the filesystem"""

    def get_data(self, data_source: str) -> dict[str, Any]:
        data = {}
        if data_source == 'users':
            data = USERS_DATA
        elif data_source == 'devices':
            data = DEVICES_DATA
        elif data_source == 'statistics':
            data = STATISTICS_DATA

        return data


class DataDbAdapter(DataInterface):
    """Imitate data retrieve from the database"""

    def get_data(self, data_source: str) -> dict[str, Any]:
        data = {}
        if data_source == 'users':
            data = USERS_DATA
        elif data_source == 'devices':
            data = DEVICES_DATA
        elif data_source == 'statistics':
            data = STATISTICS_DATA

        return data
