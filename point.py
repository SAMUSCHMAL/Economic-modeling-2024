import random

class Point:
    def _init_(self, x, y):
        self.x = x
        self.y = y


a = Point(2,3)
b = Point(7, 9)

print(f"a=({a.x},{a.y})")
print(f"b=({b.x},{b.y})")

#creating a list of 5 random points
points = [] # initialize an empty list
for _ in range(5):
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    random_point = Point(x,y)
    points.append(random_point)

    # or in a single line like this
    points.append(Point(random.randint(-100,100),
                        random.randint(-100, 100)))

for point in points:
    print(f"p{point.x},{point.y})")