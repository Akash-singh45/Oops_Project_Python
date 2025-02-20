# Route2 of inheritance in which we are creating our new properties also ,we are using super method to activate of superclasss

class Superhero:
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def use_power(self):
        print(f"{self.name} is using {self.power} power!")

    def intro_hero(self):
        print(f"I am {self.name} and I have {self.power} power!")

    def save_day(self):
        print(f"{self.name} has saved the day ")

    def power_level(self):
        length = len(self.power)
        level = length*10
        return level


class Flying(Superhero):
    def __init__(self,name,power,speed):
        super().__init__(name,power)
        self.speed = speed

    def use_power(self):
        print(f"{self.name} is flying ata the speed of {self.pedd } miles per hour")

    def calc_distance(self,flight_time):
        distance = self.speed * flight_time
        return distance



#
batman = Superhero('Batman','flight')
batman.intro_hero()
batman.save_day()
print(batman.power_level())
#







