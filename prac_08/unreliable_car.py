import random
from prac_08.car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability = 100):
        super(). __init__(fuel,name)
        #self.name=name
        #self.fuel=fuel
        self.reliability = reliability
        self.current_distance = 0

    def drive(self,distance):
        rand_num = random.randint(1,101)
        if rand_num < self.reliability:
            distance_driven = super().drive(distance)
            self.current_distance += distance_driven
        else:
            distance_driven = 0
        return distance_driven


    def __str__(self):
        return "Car class print: {}, The current distance driven by {} is {}km".format(super().__str__(),self.name,self.current_distance)