class Car:
    """ Car class with encapsulation for vehicle speed simulation"""

    def __init__(self, year_model, make):
        """
        Args:
            year_model (str/int): The car's year model
            make (str): The make of the car (e.g., Toyota, Honda, Ford)
        """
        self.__year_model = year_model
        self.__make = make
        self.speed = 0

    # Year model getter and setter
    def get_year_model(self):
        return self.__year_model

    def set_year_model(self, year_model):
        self.__year_model = year_model

    # Make getter and setter
    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    # Speed getter (no setter - speed only changes via accelerate/brake)
    def get_speed(self):
        return self.__speed

    # Accelerate method
    def accelerate(self):
        self.__speed += 5
        return self.__speed

    # Brake method
    def brake(self):
        if self.__speed >= 5:
            self.__speed -=5
        else:
            self.__speed = 0
        return self.__speed

    def __str__(self):
        return f"{self.__year_model} {self.__make} - Current Speed: {self.__speed}km/h"
    