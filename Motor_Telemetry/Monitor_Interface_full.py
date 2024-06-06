#=================================================== DRAFT CODE ===================================================#
# Mainly used for test live plotting interface

#=================================================== LIBRARIES ===================================================#
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time

import matplotx                                         # Library to change theme []
plt.style.use(matplotx.styles.dracula)


plt.rcParams["figure.figsize"] = (12, 4)
N = 2*2 ** 10
LINE_WEIGTH = 2

y=np.zeros(0,float)

y1_dc=np.zeros(0,float)
y2_rpm=np.zeros(0,float)
y3_temp=np.zeros(0,float)
y4_volt=np.zeros(0,float)
y5_current=np.zeros(0,float)

t=np.zeros(0,float)
flip=1

# Define the layout using subplot2grid
fig = plt.figure(figsize=(12, 6), tight_layout=True)
ax1_dc = plt.subplot2grid((3, 3), (0, 0), colspan=2)
ax2_rpm     = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)  # ax2 at position (1, 0)
ax3_temp    = plt.subplot2grid((3, 3), (0, 2))  # ax3 at position (0, 1)
ax4_volt    = plt.subplot2grid((3, 3), (1, 2))  # ax4 at position (1, 1)
ax5_current = plt.subplot2grid((3, 3), (2, 2))  # ax4 at position (1, 1)


def getvalues(count):
    global y,t, flip
    global y1_dc, y2_rpm, y3_temp, y31_temp_ctrl, y4_volt, y5_current

    value=500*np.sin((100 / (10*2** 10)) * 2 * np.pi * count) + 500
    y=np.append(y, value)
    y1_dc=y
    y2_rpm=y*5
    y3_temp=y*0.1
    y31_temp_ctrl=y*0.05
    y4_volt=y*0.1
    y5_current=y*0.2

    t=np.append(t, count)



def create_figure():
    line1_dc, = ax1_dc.plot([], [], lw=LINE_WEIGTH, label='DC')
    line2_rpm, = ax2_rpm.plot([], [], lw=LINE_WEIGTH, label='Left Line')
    line3_temp, = ax3_temp.plot([], [], lw=LINE_WEIGTH, label='Left Line')
    line31_tempController, = ax3_temp.plot([], [], lw=LINE_WEIGTH, label='Left Line')
    line4_volt, = ax4_volt.plot([], [], lw=LINE_WEIGTH, label='Left Line')
    line5_current, = ax5_current.plot([], [], lw=LINE_WEIGTH, label='Left Line')

    titl = ax1_dc.set_title('Left Plot Title')
    
    # Graph 1: DC
    ax1_dc.set_ylim(0, 1000)
    ax1_dc.set_xlim(0,200)
    ax1_dc.set_title('DutyCycle')
    ax1_dc.set_ylabel('Percentage [%]')
    ax1_dc.grid(True)

    # Graph 2: RPM
    ax2_rpm.set_ylim(0, 10000)
    ax2_rpm.set_xlim(0,200)
    ax2_rpm.set_title('Wheel Velocity')
    ax2_rpm.set_ylabel('Velocuty [RPM]')
    ax2_rpm.set_xlabel('time [ms]')
    ax2_rpm.grid(True)

    # Graph 3: TEMPERATURE
    ax3_temp.set_ylim(0, 150)
    ax3_temp.set_xlim(0,200)
    ax3_temp.set_title('Temperature: Motor | Motor Controller')
    ax3_temp.set_ylabel('Temperaure [°C]')
    ax3_temp.grid(True)

    # Graph 4: SUPLY VOLTAGE
    ax4_volt.set_ylim(0, 400)
    ax4_volt.set_xlim(0,200)
    ax4_volt.set_title('Supply Voltage')
    ax4_volt.set_ylabel('Voltage [V]')
    ax4_volt.grid(True)

    # Graph 1: PHASE CURRENT
    ax5_current.set_ylim(0, 256)
    ax5_current.set_xlim(0,200)
    ax5_current.set_title('Phase Current')
    ax5_current.set_ylabel('Current [A]')
    ax5_current.set_xlabel('time [ms]')
    ax5_current.grid(True)

    return (fig, ax1_dc, titl, line1_dc, line2_rpm, line3_temp,line31_tempController, line4_volt, line5_current)

def update_plot(frame, frame_times):
    global y,t
    global y1_dc, y2_rpm, y3_temp, y31_temp_ctrl, y4_volt, y5_current

    frame_times[frame] = time.perf_counter()
    getvalues(frame)
    print("Time: ",t[frame],"  volt: ",y[frame])
    time_current=t
    line1_dc.set_data(time_current      , y1_dc)
    line2_rpm.set_data(time_current     , y2_rpm)
    line3_temp.set_data(time_current    , y3_temp)
    line31_tempController.set_data(time_current , y31_temp_ctrl)
    line4_volt.set_data(time_current    , y4_volt)
    line5_current.set_data(time_current , y5_current)
    
    rescale = False
    
    if y[frame] < ax1_dc.get_ylim()[0]:
        ax1_dc.set_ylim(y[frame] - 0.1, ax1_dc.get_ylim()[1])
        rescale = True

    if y[frame] > ax1_dc.get_ylim()[1]:
        ax1_dc.set_ylim(ax1_dc.get_ylim()[0], y[frame] + 0.1)
        rescale = True

    #Update Time Axys
    if t[frame] > ax1_dc.get_xlim()[1]:
        ax1_dc.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + N / 5)
        ax2_rpm.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + N / 5)
        ax3_temp.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + N / 5)
        ax4_volt.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + N / 5)
        ax5_current.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + N / 5)
        rescale = True

    if frame == len(t) - 1:
        rescale = True
    
    if rescale:
        fig.canvas.draw()
    
    return line1_dc ,line2_rpm, line3_temp,line31_tempController, line4_volt, line5_current,

fig, ax1_dc, titl, line1_dc ,line2_rpm, line3_temp,line31_tempController, line4_volt, line5_current = create_figure()
# fig.suptitle("Motor Display")
frame_times = np.zeros(N)

#the animation is the actual loop
ani = FuncAnimation(fig, update_plot, interval=0, fargs=(frame_times,), repeat=False, frames=list(range(N)), blit=True)

#plot animation
plt.show()
