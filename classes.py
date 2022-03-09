# Programa Desenvolvido por Yuri H. Lopes
# modificado por Nicolas hehehe

import numpy as np
import math

class Complex:
    def __init__(self, realpart = 0, imagpart = 0):
        self.r = realpart
        self.i = imagpart


    def __repr__(self):
        if self.i >= 0:
            return f'{self.r} + {self.i}i'
        else:
            return f'{self.r} - {-self.i}i'


    def __abs__(self):
        z = ((self.r)**2+(self.i)**2)**1/2
        return z


    def __add__(self, other):
        r = self.r + other.r
        i = self.i + other.i
        z = Complex(r,i)
        return z


    def __mul__(self,other):
        r = (self.r)*other.r - self.i*(other.i)
        i = self.i*other.r + self.r*other.i
        z = Complex(r,i)
        return z


    def __truediv__(self, other):
        a = (other.r**2 + other.i**2)
        r = (self.r * other.r) + (self.r * other.r)
        i = (self.i * other.r) - (self.r * other.i)
        z = Complex(r/a,i/a)
        return z


    def __sub__(self, other):
        r = self.r - other.r
        i = self.i - other.i
        z = Complex(r,i)
        return z


    def __neg__(self):
        r = -self.r
        i = -self.i
        z = Complex(r,i)
        return z


class Fasor:
    def __init__(self, z, ang):
        self.z = z
        self.ang = ang


    def __repr__(self):
        return f'{self.z}∠{self.ang}°'


    def __mul__(self, other):
        z = self.z * other.z
        ang = self.ang + other.ang
        return Fasor(z,ang)


    def __truediv__(self,other):
        z = (self.z) / (other.z)
        ang = self.ang - other.ang
        return Fasor(z,ang)


    def __add__(self, other):
        a1 = (self.z) * np.sin(math.radians(self.ang))
        b1 = (self.z) * np.cos(math.radians(self.ang))
        a2 = (other.z) * np.sin(math.radians(other.ang))
        b2 = (other.z) * np.cos(math.radians(other.ang))
        r = a1 + a2
        i = b1 + b2
        z = np.sqrt(r**2 + i**2)
        ang = np.degrees((np.arctan(r/i)))
        return Fasor(z,ang)

