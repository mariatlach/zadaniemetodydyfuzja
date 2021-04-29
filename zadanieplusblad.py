import numpy as np
import matplotlib.pyplot as plt
import math

L = 1
D = 0.00001
dx = 0.1
dt = (dx**2)/(4*D)
T_pocz = 97
T_kon = 171
x_pocz = 0
x_kon = L
t_pocz = 0
t_kon = 100000
q = (D*dt)/(dx**2)
cons = 1-2*q
x = np.arange(0,x_kon + dx,dx)
t = np.arange(0,t_kon + dt,dt)
lnt = len(t) 
lnx = len(x)
T = np.zeros([lnt, lnx])
er1 = 0
er2 = 0
er = 0
for i in range(0, lnt-1):
    for n in range(0, lnx-1):
        T[:, 0] = T_pocz
        T[:, 10] = T_kon
        T[i+1, n] = q*(T[i][n+1]+T[i][n-1])+cons*T[i][n]
for n in range(0,11):
    er1 = T[i,n] - T[i+1,n]
    er1 = math.fabs(er1)
    er2 = er1/(T[i,n])
    er = er + er2
    err = er/11
print(err)
np.savetxt("dane", T, fmt="%10.5f", delimiter='\t')
X, Y = np.meshgrid(x, t, sparse=True)
plotT = plt.axes(projection='3d')
plotT.plot_surface(X, Y, T, rstride=1, cstride=1, cmap='plasma')
plotT.set_xlabel("Długosc [m]")
plotT.set_ylabel("Czas [s]")
plotT.set_zlabel("Temperatura [$^o C$]")
plotT.set_title("Wykres")
plt.show()





