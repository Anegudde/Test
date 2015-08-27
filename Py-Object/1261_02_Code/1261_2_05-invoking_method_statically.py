class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
Point.reset(p)

q =  Point()
q.x=10
q.reset()
q.y=11
print(q.x, q.y)
