class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
p.reset()

q=Point()
q.x=10
q.y=100
print q.x
print q.y
q.reset()

print(p.x, p.y)
print(q.x, q.y)
