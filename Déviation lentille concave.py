import matplotlib.pyplot as plt
import numpy as np

N=0.7
R=0.5

x=np.linspace(0,np.pi/2,1000)
## Double dioptre concave vers la droite

for i in range(1,10,2):
    R=i*10**(-1)
    y=np.sin(x)-((np.sin(x))/((np.sqrt((1-(N*np.sin(x))**2)*(1-(N*R*np.sin(x))**2))+(N**2)*R*(np.sin(x))**2)*np.sqrt(1-(R*np.sin(x))**2)-(N*np.sin(x)*np.sqrt(1-(N*R*np.sin(x))**2)-N*R*np.sin(x)*np.sqrt(1-(N*np.sin(x))**2))*R*np.sin(x)))
    plt.plot(x,y,label = f'R = {R:.2}')
    plt.legend()


plt.title("Déviation à l'entrée de la lentille")
plt.xlabel("Angle d'incidence (en rad)")
plt.show()