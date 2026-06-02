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

# Test Program
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("PET REGISTRATION SYSTEM")
    print("=" * 50)

    # Create Pet object
    my_pet = Pet()

    # Get user input
    print("\nPlease enter your pet's information:")
    print("-" * 40)

    # Get name with validation
    while True:
        try:
            name = input("Enter pet's name: ")
            my_pet.set_name(name)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    # Get animal type with validation
    while True:
        try:
            animal_type = input("Enter pet's type (Dog, Cat, Bird, etc.): ")
            my_pet.set_animal_type(animal_type)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    # Get age with validation
    while True:
        try:
            age = input("Enter pet's age (in years): ")
            my_pet.set_age(age)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    # Display pet information
    print("\n" + "=" * 50)
    print("YOUR PET'S INFORMATION")
    print("=" * 50)
    print(f" Name: {my_pet.get_name()}")
    print(f" Animal Type: {my_pet.get_animal_type()}")
    print(f" Age: {my_pet.get_age()} years")
    print(f" Summary: {my_pet.get_info()}")
    print(f" Object: {my_pet}")

    print("\n" + "=" * 50)
    print(" Pet registration completed successfully!")
    print("=" * 50)