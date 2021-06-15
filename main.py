from classes import Circle, Triangle, Square, Point

if __name__ == '__main__':
    c1 = Circle(3, 5, 5)
    c1.perimetr()
    c1.area()

    p1 = Point(2, 1)
    p2 = Point(5, 2)
    p3 = Point(1, 3)

    t1 = Triangle(p1, p2, p3)
    t1.perimetr()
    t1.area()

    p4 = Point(0, 0)
    p5 = Point(3, 0)
    p6 = Point(0, 4)

    t2 = Triangle(p4, p5, p6)
    t2.perimetr()
    print(t2.l1, t2.l2, t2.l3)
    t2.area()
