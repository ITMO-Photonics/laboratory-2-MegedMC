import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()
circle, = ax.plot([], [],'rs', ms=15)
coord = np.array([20.,90.,10.,0.])      #третья координата - вертикальная скорость
def init():
    ax.set_xlim([0., 100.])
    ax.set_ylim([-10., 100.])
    return circle,

border=2.5
g = -9.8
h = 1./50.
def eiler(coord,h,g,border):            #явный метод Эйлера
    coord[0] = coord[0] + h * coord[2]
    buf = coord[1] + h * coord[3]
    if buf < border:
        coord[3] = - coord[3] * 0.75
        coord[1]=border
    else:
        coord[1]=buf
    coord[3] = coord[3] + h * g
    if coord[0] < border or coord[0] > 100 - border:
        coord[2] = -coord[2]
    return coord
##############################
def n_eiler(coord,h,g,border):          #неявный метод Эйлера
    coord[0] = coord[0] + h * coord[2]
    coord[3] = coord[3] + h * g
    buf = coord[1] + h * coord[3]
    if buf < border:
        coord[3] = - coord[3] * 0.75
        coord[1]=border
    else:
        coord[1]=buf
    if coord[0] < border or coord[0] > 100 - border:
        coord[2] = -coord[2]
    return coord
##############################
def R_G(coord,h,g,border):          #метод Рунге-Кутты
    coord[0] = coord[0] + h * coord[2]
    buf3 = coord[3] + h * g
    buf1 = coord[1] + h * (coord[3] + buf3) / 2.
    if buf1 < border:
        buf3 = - buf3 * 0.85
        coord[1]=border
    else:
        coord[1] = buf1
    coord[3] = buf3
    if coord[0] < border or coord[0] > 100 - border:
        coord[2] = -coord[2]
    return coord
##############################

def updatefig(frame):
    eiler(coord,h,g,border)
    #R_G(coord,h,g,border)
    circle.set_xdata(coord[0])
    circle.set_ydata(coord[1])
    return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=1, init_func=init, interval=15, blit=True, repeat=True)

plt.show()
