import math

vinicial = 25
ang = 53

grav = -5

def discriminant(a, b, c): return b**2 - (4*a*c)
def cuadratic(a, b, c):
    return [(-b + math.sqrt(discriminant(a, b, c)))/(2*a),
            (-b - math.sqrt(discriminant(a, b, c)))/(2*a)]
    
vx = vinicial * math.cos(math.radians(ang))
vy = vinicial * math.sin(math.radians(ang))
dy = -12.8

t1 = cuadratic(grav, vy, -dy)[0]
t2 = cuadratic(grav, vy, -dy)[1]

t = max(cuadratic(grav, vy, -dy))

dx = vx * t

vfinal = math.hypot(vy-(grav*t),vx)

print(t1)
print(t2)
print(t)
print(vy)
print(vx)
print(dx)
print(vfinal)
#testing
