class Settings:
    def __init__(self):
        self._conn = None

    @property
    def conn(self):
        return self._conn

    @conn.setter
    def conn(self, value):
        self._conn = value


class SettingsAio:
    def __init__(self):
        self._aiocheck = False
        self._mass = None

    @property
    def aiocheck(self):
        return self._aiocheck

    @aiocheck.setter
    def aiocheck(self, value):
        self._aiocheck = value

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        self._mass = value


settings = Settings()
settingsAio = SettingsAio()
