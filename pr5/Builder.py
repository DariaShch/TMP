class Builder(object):
    def build_base(self):
        raise NotImplementedError()

    def build_lamp(self):
        raise NotImplementedError()

    def build_battery(self):
        raise NotImplementedError()

    def create_TableLamp(self):
        raise NotImplementedError()


class TableLamp(object):
    """Настольная лампа"""

    def __init__(self, base, lamp, battery):
        self._shine = False
        self._base = base
        self._lamp = lamp
        self._battery = battery

    def on(self):
        self._shine = True

    def off(self):
        self._shine = False

    def __str__(self):
        shine = 'on' if self._shine else 'off'
        return 'TableLamp [%s]' % shine


class Lamp(object):
    """Лампочка"""


class Base(object):
    """Корпус"""


class Battery(object):
    """Батарея"""


class TableLampBuilder(Builder):
    def build_base(self):
        return Base()

    def build_battery(self):
        return Battery()

    def build_lamp(self):
        return Lamp()

    def create_TableLamp(self):
        base = self.build_base()
        lamp = self.build_lamp()
        battery = self.build_battery()
        return TableLamp(base, lamp, battery)


builder = TableLampBuilder()
tablelamp = builder.create_TableLamp()
tablelamp.on()
print(tablelamp)
