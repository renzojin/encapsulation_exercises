class Fan:
    """Fan class with encapsulation and constants for speed levels"""

    # Class constants
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        """
        Args:
            speed (int): Fan speed (1, 2, or 3)
            radius (float): Fan radius
            color (str): Fan color
            on (bool): Fan power state
        """
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # Speed getter and setter
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        """
        Args:
            speed (int): Fan speed
        """
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = speed
        else:
            raise ValueError("Speed must be SLOW(1), MEDIUM(2), FAST(3)")

    # On/Off getter and setter
    def is_on(self):
        return self.__on

    def set_on(self, on):
        self.__on = on

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        """
        Args:
            radius (float): Radius value must be positive
        """

        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError("Radius must be positive")

    # Color getter and setter
    def get_color(self):
        return self.__color

    def set_color(self, color):
        if color and isinstance(color, str):
            self.__color = color
        else:
            raise ValueError("Color must be a string")

    # Helper method to get speed as string
    def get_speed_string(self):
        speed_map = {
            Fan.SLOW: "SLOW",
            Fan.MEDIUM: "MEDIUM",
            Fan.FAST: "FAST"
        }
        return speed_map.get(self.__speed, "UNKNOWN")

    def __str__(self):
        state = "ON" if self.__on else "OFF"
        return (f"Fan [Speed: {self.get_speed_string()} ({self.__speed}), "
                f"Status: {state}, Radius: {self.__radius}, Color: {self.__color}]")

# Test Program
if __name__ == "__main__":
    print("\n" + "=" * 30)
    print("FAN CLASS TEST PROGRAM")
    print("=" * 30)

    # Create first fan
    print("\nCreating Fan 1 (Maximum settings)...")
    fan1 = Fan()
    fan1.set_speed(Fan.FAST)      # Speed = 3
    fan1.set_radius(10)            # Radius = 10
    fan1.set_color("yellow")       # Color = yellow
    fan1.set_on(True)              # Turn ON

    # Create second fan
    print("\nCreating Fan 2 (Medium settings)...")
    fan2 = Fan()
    fan2.set_speed(Fan.MEDIUM)     # Speed = 2
    fan2.set_radius(5)             # Radius = 5
    fan2.set_color("blue")         # Color = blue
    fan2.set_on(False)             # Turn OFF

    # Display results
    text = "RESULTS"
    print("\n" + "=" * 30)
    print(text.center(20))
    print("=" * 30)

    print("\n🔴 FAN 1:")
    print(f"   Speed: {fan1.get_speed_string()} ({fan1.get_speed()})")
    print(f"   Status: {'ON 🟢' if fan1.is_on() else 'OFF 🔴'}")
    print(f"   Radius: {fan1.get_radius()}")
    print(f"   Color: {fan1.get_color()}")
    print(f"   {fan1}")

    print("\n🔵 FAN 2:")
    print(f"   Speed: {fan2.get_speed_string()} ({fan2.get_speed()})")
    print(f"   Status: {'ON 🟢' if fan2.is_on() else 'OFF 🔴'}")
    print(f"   Radius: {fan2.get_radius()}")
    print(f"   Color: {fan2.get_color()}")
    print(f"   {fan2}")

    print("\n" + "=" * 50)
    print("Test completed successfully!")
    print("=" * 50)