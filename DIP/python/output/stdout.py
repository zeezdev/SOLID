"""Output level. Depend on data interfaces """
import sys

from DIP.python.core.models import User, Device, StatisticLog


class StdoutOutput:

    def out_users(self, users: list[User]) -> None:
        for u in users:
            sys.stdout.write(f'{u.username}\n')

    def out_devices(self, devices: list[Device]) -> None:
        for d in devices:
            sys.stdout.write(f'{d.name}\n')

    def out_statistics(self, statistics: list[StatisticLog]) -> None:
        sys.stdout.write(f'Statistics count: {len(statistics)}\n>')
