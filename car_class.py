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

    