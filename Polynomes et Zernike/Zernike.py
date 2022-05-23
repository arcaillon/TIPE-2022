import math

def Rmn(m,n,rho):
    if (n-m) % 2 == 0:
        R = 0
        for k in range((n-m)/2+1):
            R += ((-1)**k*math.fact(n-k)) / (math.fact(k)*math.fact((n+m)/2-k)*math.fact((n-m)/2-k))*rho**(n-2*k)
    return R

def Zernike(m,n,rho,phi):
    if m > 0 :
        return Rmn(m,n,rho)*math.cos(m*phi)
    else :
        return Rmn(m,n,rho)*math.sin(m*phi)
