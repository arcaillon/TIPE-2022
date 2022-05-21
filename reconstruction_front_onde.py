from Exp_SH import *
import numpy as np
from math import sqrt, atan


def calcule_angle_incident(dx,dy,d_focale):
    return atan(sqrt(dx*dx+dy*dy)/d_focale)

def calcule_angles_incidents(mes_exp,pas,d_focale):
    angles = []
    for l in mes_exp:
        a1 = []
        for e in l:
            a1.append(calcule_angle_incident(e[0],e[1],d_focale))
        angles.append(a1)
    return angles

print(calcule_angles_incidents(mesure_experience,pas,focale_experience))