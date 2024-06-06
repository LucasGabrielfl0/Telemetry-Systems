#=================================================== DRAFT CODE ===================================================#
# Mainly used for test live plotting interface

#=================================================== LIBRARIES ===================================================#
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time

plt.rcParams["figure.figsize"] = (12, 4)
N = 10*2 ** 10
LINE_WEIGTH = 2

y=np.zeros(0,float)
t=np.zeros(0,float)
flip=1

fig, axL = plt.subplots(figsize=(6, 4), tight_layout=True)

def getvalues(count):
    global y,t, flip

    if flip==1:
        y=np.append(y, 1.0)
        flip=0
    else:
        y=np.append(y, 0.0)
        flip=1
    t=np.append(t, count)



def create_figure():
    linel, = axL.plot([], [], lw=LINE_WEIGTH, label='Left Line')
    titl = axL.set_title('Left Plot Title')

    axL.set_ylim(0,2.2)
    axL.set_xlim(0,200)
    axL.set_xlabel("TIME")
    axL.set_ylabel("RPM")
    axL.grid(True)


    return (fig, axL, titl, linel)

def update(frame, frame_times):
    global y,t
    frame_times[frame] = time.perf_counter()
    
    getvalues(frame)
    print("Time: ",t[frame],"  volt: ",y[frame])
    linel.set_data(t, y)
    
    rescale = False
    if y[frame] < axL.get_ylim()[0]:
        axL.set_ylim(y[frame] - 0.1, axL.get_ylim()[1])
        rescale = True
    if y[frame] > axL.get_ylim()[1]:
        axL.set_ylim(axL.get_ylim()[0], y[frame] + 0.1)
        rescale = True
    if t[frame] > axL.get_xlim()[1]:                                 #Update Time Axys
        axL.set_xlim(axL.get_xlim()[0], axL.get_xlim()[1] + N / 5)
        rescale = True
    if frame == len(t) - 1:
        rescale = True
    
    if rescale:
        fig.canvas.draw()
    
    return linel,

fig, axL, titl, linel = create_figure()
fig.suptitle("Motor Display")
frame_times = np.zeros(N)

#the animation is the actual loop
ani = FuncAnimation(fig, update, interval=500, fargs=(frame_times,), repeat=False, frames=list(range(N)), blit=True)

#plot animation
plt.show()
