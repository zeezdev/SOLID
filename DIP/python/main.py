from DIP.python.data.adapters import DataFileAdapter, DataDbAdapter
from DIP.python.data.providers import DataProvider
from DIP.python.core.services import UserService, DeviceService, StatisticsService
from DIP.python.output.stdout import StdoutOutput


class Main:
    """This is a 'dirty class' that knows everything about everyone"""

    def run(self):
        user_service = UserService(provider=DataProvider(data_adapter=DataFileAdapter()))
        active_users = user_service.get_active_users()

        provider = DataProvider(data_adapter=DataDbAdapter())

        device_service = DeviceService(provider=provider)
        siemens_devices = device_service.get_devices_by_manufacturer('Siemens')

        statistics_service = StatisticsService(provider=provider)
        user_statistics = statistics_service.get_device_statistics_for_users(username='jdoe')

        output = StdoutOutput()
        output.out_users(active_users)
        output.out_devices(siemens_devices)
        output.out_statistics(user_statistics)


if __name__ == '__main__':
    Main().run()
