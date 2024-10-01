class Temp_out:
    def __init__(self,temp_out):
        self.temp_out = temp_out
    def temp(self):
        return self.temp_out
class Temp_in:
    def __init__(self,temp_in):
        self.temp_in = temp_in
    def temp_home(self):
        return self.temp_in
class Baro_out:
    def __init__(self, baro):
        self.baro = baro
    def baro_out(self):
        return self.baro

class Weather(Temp_out, Temp_in, Baro_out ):
    def __init__(self, temp_out, temp_in, baro):
         Temp_out.__init__(self, temp_out)
         Temp_in.__init__(self, temp_in)
         Baro_out.__init__(self, baro)
        
klimat = Weather(20, 25, 746)
print(f'Температура на улице: {klimat.temp()} градусов')
print(f'Температура в доме: {klimat.temp_home()} градусов')
print(f'Атмосферное давление: {klimat.baro_out()} мм.рт.ст')