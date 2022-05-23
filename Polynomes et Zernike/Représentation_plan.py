#from Polynomes import *

def calc_z_coin (t,f, pasx,pasy) :
    m = len(t)
    n = len(t[0])
    Z = [[0 for _ in range (n)] for _ in range (m)]
    for i in range (1,n):
        X,Y = t[0][i-1]
        Z[0][i]=Z[0][i-1]-X/f*pasx
    for i in range (1,m):
        X,Y = t[i-1][0]
        Z[i][0]=Z[i-1][0]-Y/f*pasy
    for i in range (1,m):
        for j in range (1,n):
            X1,Y1=t[i][j-1]
            X2, Y2 = t[i-1][j]
            Z[i][j] = 0.5*(Z[i][j-1]-X1/f*pasx + Z[i-1][j]-Y2/f*pasy)
    return Z

def calc_z_centre (t,f, pasx,pasy) :
    m = len(t)
    n = len(t[0])
    Z = [[0 for _ in range (n)] for _ in range (m)]
    if m  % 2 ==0 :
        m1=m//2
    else:
        m1=m//2 + 1
    if n%2 == 0:
        n1=n//2
    else :
        n1=n//2 + 1
    for i in range (n1,n):
        X,Y = t[m1][i-1]
        Z[m1][i]=Z[m1][i-1]-X/f*pasx
    for i in range (n1-1,-1,-1):
        X,Y = t[m1][i+1]
        Z[m1][i]=Z[m1][i+1]+X/f*pasx
    for i in range (m1,m):
        X,Y = t[i-1][n1]
        Z[i][n1]=Z[i-1][n1]-Y/f*pasy
    for i in range (m1,-1,-1):
        X,Y = t[i+1][n1]
        Z[i][n1]=Z[i+1][n1]+Y/f*pasy
    for i in range (m1,m):
        for j in range (n1,n):
            X1,Y1=t[i][j-1]
            X2, Y2 = t[i-1][j]
            Z[i][j] = 0.5*(Z[i][j-1]-X1/f*pasx + Z[i-1][j]-Y2/f*pasy)
    for i in range (m1,m):
        for j in range (n1-1,-1,-1):
            X1,Y1=t[i][j+1]
            X2, Y2 = t[i-1][j]
            Z[i][j] = 0.5*(Z[i][j+1]+X1/f*pasx + Z[i-1][j]-Y2/f*pasy)
    for i in range (m1-1,-1,-1):
        for j in range (n1,n):
            X1,Y1=t[i][j-1]
            X2, Y2 = t[i+1][j]
            Z[i][j] = 0.5*(Z[i][j-1]-X1/f*pasx + Z[i+1][j]+Y2/f*pasy)
    for i in range (m1-1,-1,-1):
        for j in range (n1-1,-1,-1):
            X1,Y1=t[i][j+1]
            X2, Y2 = t[i+1][j]
            Z[i][j] = 0.5*(Z[i][j+1]+X1/f*pasx + Z[i+1][j]+Y2/f*pasy)
    return Z

t=[[(0,0),(-1,-1),(0,1),(-1,1),(-1,0),(1,1),(-1,0),(-1,1),(-1,0),(-1,1),(-1,1),(-1,2),(0,0)],
   [(2,1),(1,1),(0,0),(-1,0),(-2,0),(-1,0),(0,0),(0,0),(0,-1),(-1,1),(-1,1),(-2,1),(-2,1)],
   [(1,0),(0,0),(0,1),(-2,0),(-2,-1),(-1,2),(0,1),(0,0),(-1,1),(0,-1),(0,1),(-1,1),(-1,3)],
   [(1,0),(0,0),(0,0),(-2,-1),(0,-1),(1,-1),(0,-1),(0,-1),(0,0),(0,-1),(-2,-1),(-1,0),(-1,0)],
   [(2,0),(0,-1),(0,0),(-2,0),(-1,0),(0,0),(1,0),(1,0),(-1,-2),(0,0),(0,0),(-1,-1),(-1,0)],
   [(1,0),(0,0),(1,0),(-1,0),(0,0),(0,0),(0,0),(0,-1),(0,0),(0,0),(2,0),(-1,1),(-1,-1)],
   [(1,0),(0,0),(2,0),(-1,0),(0,0),(0,0),(-2,2),(0,0),(0,0),(-1,0),(-1,1),(0,0),(-1,-1)],
   [(2,-2),(0,0),(1,-1),(0,-1),(0,0),(0,0),(0,0),(0,0),(-1,0),(0,0),(0,-1),(-2,0),(-1,-1)],
   [(1,-1),(-1,1),(1,0),(-1,0),(0,0),(0,0),(0,-1),(0,0),(0,0),(0,0),(-1,0),(-1,-1),(-2,-1)],
   [(0,0),(1,-1),(-1,0),(2,0),(0,0),(0,-1),(0,0),(0,0),(0,0),(0,0),(0,-1),(0,0),(0,0)],
   [(0,0),(1,-1),(-1,0),(1,-2),(0,-1),(1,-1),(0,0),(0,-1),(0,-1),(-1,-1),(0,0),(0,0),(0,0)]]


plan_z1=calc_z_centre(t,20,5,5)
n1=len(plan_z1[0])
m1=len(plan_z1)
lx=[i+0.5 for i in range (m1)]
ly=[j+0.5 for j in range (n1)]


z1=interpole2v(lx,ly,plan_z1)

def plan1 (x,y):
    val=0
    n=len(z1)
    m=len(z1[0])
    for i in range (n):
        for j in range (m):
            val += x**i * y**j * z1[i][j]
    return val

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
ax = Axes3D(plt.figure())
plan1=np.vectorize(plan1)
X = np.arange(0, 5, 0.1)
Y = np.arange(0, 5, 0.1)
X, Y = np.meshgrid(X, Y)
Z = plan1(X, Y)
ax.plot_surface(X, Y, Z)
plt.show()

plan_z2=calc_z_coin(t,20,5,5)
n2=len(plan_z2[0])
m2=len(plan_z2)
lx=[i+0.5 for i in range (m2)]
ly=[j+0.5 for j in range (n2)]


z2=interpole2v(lx,ly,plan_z2)

def plan2 (x,y):
    val=0
    n=len(z2)
    m=len(z2[0])
    for i in range (n):
        for j in range (m):
            val += x**i * y**j * z2[i][j]
    return val


ax = Axes3D(plt.figure())
plan2=np.vectorize(plan2)
X = np.arange(0, 5, 0.1)
Y = np.arange(0, 5, 0.1)
X, Y = np.meshgrid(X, Y)
Z = plan2(X, Y)
Z[0] = 0
ax.plot_surface(X, Y, Z)
plt.show()


tb=[[(1,1),(0,0),(-1,0),(-2,0),(-1,0),(0,0),(0,0),(0,-1),(-1,1),(-1,1),(-2,1)],
   [(0,0),(0,1),(-2,0),(-2,-1),(-1,2),(0,1),(0,0),(-1,1),(0,-1),(0,1),(-1,1)],
   [(0,0),(0,0),(-2,-1),(0,-1),(1,-1),(0,-1),(0,-1),(0,0),(0,-1),(-2,-1),(-1,0)],
   [(0,-1),(0,0),(-2,0),(-1,0),(0,0),(1,0),(1,0),(-1,-2),(0,0),(0,0),(-1,-1)],
   [(0,0),(1,0),(-1,0),(0,0),(0,0),(0,0),(0,-1),(0,0),(0,0),(2,0),(-1,1)],
   [(0,0),(2,0),(-1,0),(0,0),(0,0),(-2,2),(0,0),(0,0),(-1,0),(-1,1),(0,0)],
   [(0,0),(1,-1),(0,-1),(0,0),(0,0),(0,0),(0,0),(-1,0),(0,0),(0,-1),(-2,0)],
   [(-1,1),(1,0),(-1,0),(0,0),(0,0),(0,-1),(0,0),(0,0),(0,0),(-1,0),(-1,-1)],
   [(1,-1),(-1,0),(2,0),(0,0),(0,-1),(0,0),(0,0),(0,0),(0,0),(0,-1),(0,0)]]

plan_z3=calc_z_centre(tb,20,5,5)
n3=len(plan_z3[0])
m3=len(plan_z3)
lx3=[i+0.5 for i in range (m3)]
ly3=[j+0.5 for j in range (n3)]


z3=interpole2v(lx3,ly3,plan_z3)

def plan3 (x,y):
    val=0
    n=len(z3)
    m=len(z3[0])
    for i in range (n):
        for j in range (m):
            val += x**i * y**j * z3[i][j]
    return val

ax = Axes3D(plt.figure())
plan3=np.vectorize(plan3)
X = np.arange(0, 5, 0.1)
Y = np.arange(0, 5, 0.1)
X, Y = np.meshgrid(X, Y)
Z = plan3(X, Y)
Z[0] = 0
ax.plot_surface(X, Y, Z)
plt.show()