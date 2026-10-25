from point import Point


def test_two_zero_points_equal():
    point1 = Point(0, 0)
    point2 = Point(0, 0)

    assert point1 == point2

def test_two_different_points_dont_equal():
    point1 = Point(0, 0)
    point2 = Point(180, 90)

    assert point1 != point2
