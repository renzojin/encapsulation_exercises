class Pet:
    """Pet class with encapsulation for pet information management"""

    def __init__(self, name="", animal_type="", age=0):
        """
        Args:
            name (str): Name of the pet
            animal_type (str): Animal type of the pet
            age (int): Age of the pet in years
        """
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Name getter and setter
    def get_name(self):
        return self.__name

    def set_name(self, name):
        """
        Args:
            name (str): Name of the pet
        """
        if name and name.strip():
            self.__name = name.strip()
        else:
            raise ValueError("Name cannot be empty")

    # Animal type getter and setter
    def get_animal_type(self):
        return self.__animal_type

    def set_animal_type(self, animal_type):
        """
        Args:
            animal_type (str): Animal type of the pet
        """
        if animal_type and animal_type.strip():
            self.__animal_type = animal_type.strip()
        else:
            raise ValueError("Animal type cannot be empty")

    # Age getter and setter
    def get_age(self):
        return self.__age

    def set_age(self, age):
        """
        Args:
            age (int): Age of the pet in years
        """
        try:
            age = int(age)
            if age >= 0:
                self.__age = age
            else:
                raise ValueError("Age cannot be negative")
        except ValueError:
            raise ValueError("Age cannot be negative")

    # Helper methods
    def get_info(self):
        return f"{self.__name} the {self.__animal_type} is {self.__age} years old"

    def __str__(self):
        return f"Pet(name='{self.__name}', animal_type='{self.__animal_type}', age={self.__age})"
    