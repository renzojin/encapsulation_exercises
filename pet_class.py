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