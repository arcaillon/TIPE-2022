from Exp_SH import *
import numpy as np
from math import sqrt, atan
import random
import matplotlib.pyplot as plt
from matplotlib import cm


def calcule_vecteur_incident(dx,dy,d_focale):
    O = np.array([d_focale,0,0])
    M = np.array([0,dx,dy])
    OM = M - O
    N =  np.sqrt(np.dot(OM,OM))
    OM = OM / N
    return OM


def calcule_vecteurs_incidents(mes_exp,pas,d_focale):
    vecteurs = []
    for l in mes_exp:
        v = []
        for e in l:
            v.append(calcule_vecteur_incident(e[0],e[1],d_focale))
        vecteurs.append(v)
    return vecteurs

def calcule_image_deformation(dx,dy):
    return np.sqrt(dx*dx+dy*dy)

def calcule_image_deformations(mes_exp):
    deformations = []
    for l in mes_exp:
        d = []
        for e in l:
            d.append(calcule_image_deformation(e[0],e[1]))
        deformations.append(d)
    return deformations

def calcule_polynome(vis):
    vi = vis[0][1]
    vix = np.array((vi[0],vi[1]))
    vixu = vix / (np.sqrt(np.dot(vix,vix)))
    vtx = np.array((-vixu[1],vixu[0]))
    dpx = vtx[0]

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

def calcul_point_image(forme_lentille,i,j,pas,d_focale):
    dx = (forme_lentille[i+1+1][j+1]-forme_lentille[i][j+1])/(pas*2)
    dy = (forme_lentille[i+1][j+1+1]-forme_lentille[i+1][j])/(pas*2)
    vi = np.array((np.sqrt(1-dx*dx-dy*dy),dx,dy))
    OM = vi * d_focale / vi[0]
    return OM[1],OM[2]

def calcule_points_image(forme_lentille,pas,d_focale):
    return [[calcul_point_image(forme_lentille,i,j,pas,focale_experience) for i in range(len(forme_lentille)-2)] for j in range(len(forme_lentille[0])-2)]

def calcule_cumulerreur(forme_lentille,mesure,pas,d_focale):

    # try:
    #     calcule_cumulerreur.surf.remove()
    # except:
    #     calcule_cumulerreur.fig = plt.figure()
    #     calcule_cumulerreur.ax = calcule_cumulerreur.fig.add_subplot(111,projection='3d')
    #     #calcule_cumulerreur.fig.clear()
    #     calcule_cumulerreur.fig.show()
    #     plt.draw()
    #     plt.ion()

    s = 0

    for i in range(len(mesure)):
        for j in range(len(mesure[0])):
            dx,dy = calcul_point_image(forme_lentille,i,j,pas,d_focale)
            ex = dx - mesure[i][j][0]
            ey = dy - mesure[i][j][1]
            e = np.sqrt(ex*ex+ey*ey)
            s += e
    #print(Z,forme_lentille)
    # X,Y = np.meshgrid(X,Y)
    # Z = np.array(Z)
    # calcule_cumulerreur.surf = calcule_cumulerreur.ax.plot_surface(X,Y,Z,cmap = cm.coolwarm)
    # plt.draw()
    # plt.show()
    # calcule_cumulerreur.fig.canvas.draw()
    return s

def optim(forme_lentille,mesure,pas,d_focale):
    r = calcule_cumulerreur(forme_lentille,mesure,pas,d_focale)
    while True:
        i = random.randrange(0,len(mesure))
        j = random.randrange(0,len(mesure[0]))
        v = random.random() - 0.5
        v = v/10
        forme_lentille[i][j] += v
        rn = calcule_cumulerreur(forme_lentille,mesure,pas,d_focale)
        if rn < r :
            r = rn
            print(r)
            if (r<1.0):
                return forme_lentille
        else:
            forme_lentille[i][j] -= v





#print(calcule_angles_incidents(mesure_experience,pas,focale_experience))
#print(calcule_vecteurs_incidents(mesure_experience,pas,focale_experience))
#vi = calcule_vecteurs_incidents(mesure_experience,pas,focale_experience)
#calcule_polynome(vi)
#print(calcule_image_deformations(mesure_experience))
mesure_experience = [[mesure_experience[i][j] for i in range(2)] for j in range(2)]
forme_lentille = [[0 for i in range(len(mesure_experience[0])+2)] for j in range(len(mesure_experience)+2)]
#print(optim(forme_lentille,mesure_experience,pas,focale_experience))

forme_lentille=[[1, 0,0, 0], [0.0,0, 0,0], [0, 0, 0,0],[0,0,0,0]];print(forme_lentille,calcule_points_image(forme_lentille,pas,focale_experience),mesure_experience)
forme_lentille=[[0, 1,0, 0], [0.0,0, 0,0], [0, 0, 0,0],[0,0,0,0]];print(forme_lentille,calcule_points_image(forme_lentille,pas,focale_experience),mesure_experience)
forme_lentille=[[0, 0,1, 0], [0.0,0, 0,0], [0, 0, 0,0],[0,0,0,0]];print(forme_lentille,calcule_points_image(forme_lentille,pas,focale_experience),mesure_experience)
forme_lentille=[[0, 0,0, 1], [0.0,0, 0,0], [0, 0, 0,0],[0,0,0,0]];print(forme_lentille,calcule_points_image(forme_lentille,pas,focale_experience),mesure_experience)

exit(0)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
fig.show()
Z = np.array([[np.sqrt(__[0]*__[0]+__[1]*__[1]) for __ in _]  for _ in mesure_experience])
X = np.linspace(0,1,len(mesure_experience))
Y = np.linspace(0,1,len(mesure_experience[0]))
X,Y = np.meshgrid(X,Y)
ax.plot_surface(X,Y,Z,cmap = cm.coolwarm)
plt.show()