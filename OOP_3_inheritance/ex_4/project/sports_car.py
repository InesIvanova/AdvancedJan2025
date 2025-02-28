from project.car import Car


class SportsCar(Car):
    def race(self):
        return "racing..."


sp = SportsCar()
print(sp.drive())