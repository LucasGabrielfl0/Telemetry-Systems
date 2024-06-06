#=================================================== DRAFT CODE ===================================================#
# Mainly used for test live plotting interface

#=================================================== LIBRARIES ===================================================#
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time

plt.rcParams["figure.figsize"] = (12, 4)
volt= 10
N = 10*2 ** 10
lwL = 2
axRxlims = [0, N]
axRylims = [0, 160]


count=0.1
y=np.zeros(0,float)
t=np.zeros(0,float)

y=np.append(y, 0)
t=np.append(t, 0)
flip=1


def getvalues(count):
    global y,t, flip

    if flip==1:
        y=np.append(y, 1.0)
        flip=0
    else:
        y=np.append(y, 0.0)
        flip=1
    t=np.append(t, count)


fig, axL = plt.subplots(figsize=(6, 4), tight_layout=True)

def getfigax():
    linel, = axL.plot([], [], lw=lwL, label='Left Line')
    titl = axL.set_title('Left Plot Title')

    axL.set_ylim(0,2.2)
    axL.set_xlim(0,200)
    axL.set_xlabel("distance")
    axL.set_ylabel("Terrain Height (m)")
    axL.grid(True)


    return (fig, axL, titl, linel)

def update(frame, frame_times):
    global y,t
    frame_times[frame] = time.perf_counter()
    
    # print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa : frame: ", frame)
    getvalues(frame)
    print("Time: ",t[frame],"  volt: ",y[frame])
    linel.set_data(t, y)
    # print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa : flag 2 ", frame)
    
    # titl.set_text(f"Frame: {N - frame}")
    
    rescale = False
    # rescale= True
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
    
    return linel, titl

fig, axL, titl, linel = getfigax()
fig.suptitle("Func Animation: Blitting Intelligent ax update")
frame_times = np.zeros(N)

#the animation is the actual loop
ani = FuncAnimation(fig, update, interval=500, fargs=(frame_times,), repeat=False, frames=list(range(N)), blit=True)

#plot animation
plt.show()
