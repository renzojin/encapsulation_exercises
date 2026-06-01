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

    def get_color(self):
        return self.__color

    def set_color(self, color):
        if color and isinstance(color, str):
            self.__color = color
        else:
            raise ValueError("Color must be a string")

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


