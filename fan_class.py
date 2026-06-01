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
        self.speed = speed
        self.on = on
        self.radius = radius
        self.color = color