from math import cos, sin


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x is {str(self.x)}, y is {str(self.y)}"

    class PointFactory:
        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))


if __name__ == "__main__":
    my_point = Point(2, 3)
    my_point_factory = my_point.PointFactory()
    p1 = my_point_factory.new_cartesian_point(my_point.x, my_point.y)
    p2 = my_point_factory.new_polar_point(my_point.x, my_point.y)
    print("with new_cartesian_point:", p1)
    print("with new_polar_point:", p2)
