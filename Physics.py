import math

class Physics:

    def __init__(self, mass: float, density: float):

        #масса физического тела в килограммах (по системе СИ)
        self.__mass = mass 
        
        #плотность физического тела
        self.__density = density

        #импульс физического тела
        self.__impulse = 0 

        #кинетическая энергия физического тела
        self.__kinetic_e = 0

        #эластичность физического тела
        self.__elasticity = 0.5

        #скорость физического тела
        self.__velocity = 0

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, value):
        return self.__velocity

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, value):
        self.__mass = value

    @property
    def density(self):
        return self.__density

    @density.setter
    def density(self, value):
        self.__density = value

    @property
    def impulse(self):
        return self.__impulse

    @impulse.setter
    def impulse(self, value):
        self.__impulse = value

    @property
    def kinetic_e(self):
        return self.__kinetic_e

    @kinetic_e.setter
    def kinetic_e(self, value):
        self.__kinetic_e = value

    @property
    def elasticity(self):
        return self.__elasticity

    @elasticity.setter
    def elasticity(self, value):
        self.__elasticity = value

    