import numpy as np


class Vector(np.ndarray):
    def __new__(cls, x: float, y: float):
        obj = np.asarray([x, y]).view(cls)
        obj.x = x
        obj.y = y
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return
        self.x = getattr(obj, "x", None)
        self.y = getattr(obj, "y", None)
    

class Particle:
    def __init__(self, r: list, v: list, dt: float):
        self.r = Vector(*r)
        self.v = Vector(*v)
        self.dt = dt


    def __str__(self):
        return f"r: {self.r}\nv: {self.v}"


    @property
    def direction(self):
        return np.array([self.dt if 0.0 <= self.r.x <= 10.0 else -self.dt,
                         self.dt if 0.0 <= self.r.y <= 10.0 else -self.dt])



particle = Particle(r=[1.0, 3.0], v=[0.4, -0.23], dt=0.01)
particle.r = particle.r + particle.v * particle.dt

print(particle.r)
