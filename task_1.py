class Circle:
    """
    A class representing a circle.
    Attributes:
        all_circles (list): a list of all created instances of the class.
        pi (float): the value of pi number.
    """
    all_circles = []
    pi = 3.1415
    def __init__(self, radius=1) -> None:
        """
        Initializes an instance of a circle with the specified radius.
        The created instance is added to the all_circles list.
        Args:
            radius the radius of the circle. The default value is 1.
        """
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self) -> float:
        """
        Calculates the area of a circle.

        Returns:
            float: the area of a circle.
        """
        return Circle.pi * self.radius ** 2

    @staticmethod
    def total_area() -> float:
        """
        Calculates the total area of all created circle instances.

        Returns:
            float: the sum of the areas of all circles in the all_circles list.
        """
        return sum(circle.area() for circle in Circle.all_circles)

    def __str__(self) -> str:
        """
        Returns a string representation of the circle's radius.
        """
        return str(self.radius)

    def __repr__(self) -> str:
        """
        Returns a string representation of the object
        that is used when displaying it in containers
        """
        return str(self.radius)


c1 = Circle()
c2 = Circle(7)
c3 = Circle(5)
print(c2.area())
print(c3)
print(Circle.pi)
print(Circle.all_circles)
print(Circle.total_area())
print(len(c3.__class__.all_circles))
