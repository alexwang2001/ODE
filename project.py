from vpython import *

s = sphere(pos = vec(-10,0,0), color = color.gray)

t = 0
dt = 0.01
v = 2

while t < 10:
    s.pos.x += v * dt
    t += dt
    rate(30)

