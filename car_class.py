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
        self.__speed = 0

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
        return f"{self.__year_model} {self.__make} - Current Speed: {self.__speed} km/h"


# Test Program
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("CAR SPEED SIMULATOR")
    print("=" * 60)

    # Get car information from user
    print("\nEnter your car details:")
    print("-" * 40)
    year = input("Enter car's year model: ")
    make = input("Enter car's make (e.g., Toyota, Honda, Ford): ")

    # Create Car object
    my_car = Car(year, make)

    print(f"\n Created: {my_car}")

    # Accelerate 5 times
    print("\n" + "=" * 60)
    print("ACCELERATION PHASE (5 times)")
    print("=" * 60)

    for i in range(1, 6):
        current_speed = my_car.accelerate()
        print(f"   Acceleration {i}: Speed = {current_speed} km/h")

    # Brake 5 times
    print("\n" + "=" * 60)
    print("BRAKING PHASE (5 times)")
    print("=" * 60)

    for i in range(1, 6):
        current_speed = my_car.brake()
        print(f"   Brake {i}: Speed = {current_speed} km/h")

    # Final summary
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    print(f"   Car: {my_car.get_year_model()} {my_car.get_make()}")
    print(f"   Final Speed: {my_car.get_speed()} km/h")
    print(f"   {my_car}")

    print("\n" + "=" * 60)
    print("Simulation completed successfully!")
    print("=" * 60)