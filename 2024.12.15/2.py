from decimal import Decimal
from datetime import time, date, datetime, timedelta

class PowerMeter:
    def __init__(self):
        self.__tariff1 = Decimal(6.5)
        self.__tariff2 = Decimal(5.2)
        self.tariff2_starts = time(23, 0, 0)
        self.tariff2_ends = time(6, 0, 0)
        self.power = Decimal(0)
        self.charges = {date.today().isoformat()[:7]: Decimal(0)} # date.today().month: 0
       
    @property
    def tariff1(self):
        return self.__tariff1
       
    @tariff1.setter
    def tariff1(self, new_tariff):
        self.__tariff1 = Decimal(new_tariff)
        
    @property
    def tariff2(self):
        return self.__tariff2
       
    @tariff2.setter
    def tariff2(self, new_tariff):
        self.__tariff2 = Decimal(new_tariff)
        
    def get_tariff(self):
        FMT = '%H:%M:%S'
        td2 = datetime.strptime(self.tariff2_ends.isoformat(), FMT) - datetime.strptime(self.                   tariff2_starts.isoformat(), FMT)
        td2 = Decimal(td2.seconds / 3600)
        td1 = 24 - td2
        tariff = (self.__tariff1 * td1 + self.__tariff2 * td2) / 24
        return tariff
        
    def __repr__(self):
        sum_val = round(sum(self.charges.values()), 2)
        return f"<PowerMeter: {sum_val} кВт/ч>"
        
    def __str__(self):
        sum_val = round(sum(self.charges.values()) * self.get_tariff() ,2)
        return f"({date.today():%b}) {sum_val}"
        
    def meter(self, power):
        add_power = Decimal(power)
        self.charges[date.today().isoformat()[:7]] += add_power
        return round(add_power * self.get_tariff(), 2)
        
        

# >>> pm1 = PowerMeter()
# >>> pm1.meter(2)
# Decimal('12.24')
# >>> pm1.meter(1.2)
# Decimal('7.34')
# >>> pm1
# <PowerMeter: 3.20 кВт/ч>
# >>> print(pm1)
# (Jan) 19.59