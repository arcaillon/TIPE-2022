from scipy.integrate import dblquad
from Zernike import *
from Représentation_plan import *

def ps(f,g,domaine_x,domaine_y):
    return dblquad(lambda x, y : f(x,y)*g(x,y), domaine_y[0], domaine_y[1], lambda x: domaine_x[0], lambda x: domaine_x[1])

plan_z1=calc_z_centre(t,200,5,5)
lx=[i+0.5 for i in range (m1)]
ly=[j+0.5 for j in range (n1)]

z1=interpole2v(lx,ly,plan_z1)
projection_zernike = []
for n in range(6):
    pr = []
    for m in range(n+1):
        pr.append(ps(Zernike(m,n,rho,phi),z1,[0,5],[0,5]))
    projection_zernike.append(pr)
print (projection_zernike)
