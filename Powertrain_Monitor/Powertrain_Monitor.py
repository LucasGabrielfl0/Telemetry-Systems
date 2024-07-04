#=================================================== MOTOR TELEMETRY SYSTEM ===================================================#
 # Capibarib E-racing
 # Federal University of Pernambuco (UFPE)
 # Group Area: Powertrain
 
 # This file contains the Motor/Controller Telemetry system [Monitoring Interface] for tests in the Laboratory.
 # Details of the Physical connections and the circuit can be found on the Github or the Team's Google Drive
 
# This Serial Read has 2 distinct Modes: USB_READ and RS232_READ

#=================================================== LIBRARIES ===================================================#
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation          # Animation
import matplotx                                         # Library to change theme []
plt.style.use(matplotx.styles.dracula)

import numpy as np
import time

# Custom Libs
from Datalogger     import *
from SerialReader   import *
from SineTest       import *
from PlotSettings   import *


TEST_MODE = False
if TEST_MODE:
    ReadSerial  =   ReadTest
    NewArrays   =   NewArraysTest
else:
    ReadSerial  =   ReadSerial
    NewArrays   =   NewArrays



#================================================ PLOT UPDATE: BLITING + AUTO AXYS ================================================#
# Animated Plot
def update_plot(frame, frame_times):
    global time_data, start_time
    global y1_dc, y2_rpm, y30_Tm, y31_Tc, y4_volt, y5_current

    # Update Values
    start_time,time_data, y1_dc, y2_rpm, y30_Tm, y31_Tc, y4_volt, y5_current = ReadSerial(start_time,time_data, y1_dc, y2_rpm, y30_Tm, y31_Tc, y4_volt, y5_current)
    
    if time_data[0]>0:
        start_time= time_data[0]
        time_data = time_data - start_time


    frame_times[frame] = time.perf_counter()
    print("Time: ",time_data[frame],"  volt: ",y1_dc[frame])

    # Update Lines in the Plot
    line1_dc.set_data(time_data      , y1_dc)
    line2_rpm.set_data(time_data     , y2_rpm)
    line30_Tm.set_data(time_data     , y30_Tm)
    line31_Tc.set_data(time_data     , y31_Tc)
    line4_volt.set_data(time_data    , y4_volt)
    line5_current.set_data(time_data , y5_current)
    
    rescale = False

    # If y out of Lower bounds, rescales
    if y1_dc[frame] < ax1_dc.get_ylim()[0]:
        ax1_dc.set_ylim(y1_dc[frame] - 0.1, ax1_dc.get_ylim()[1])
        rescale = True

    # If y out of Upper bounds, rescales
    if y1_dc[frame] > ax1_dc.get_ylim()[1]:
        ax1_dc.set_ylim(ax1_dc.get_ylim()[0], y1_dc[frame] + 0.1)
        rescale = True

    # If time out of bounds, updates Time Axys
    if time_data[frame] > ax1_dc.get_xlim()[1]:
        ax2_rpm.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + XLIM_MAX / 5)
        ax3_temp.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + XLIM_MAX / 5)
        ax4_volt.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + XLIM_MAX / 5)
        ax5_current.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + XLIM_MAX / 5)
        ax1_dc.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + XLIM_MAX / 5)
        rescale = True

    if frame == len(time_data) - 1:
        rescale = True
    
    if rescale:                 # If graph is out of bounds, redraws graph
        fig.canvas.draw()

    if frame==MAX_FRAMES-1:     # If the graph got to the Last frame, saves the arrays and resets them
        time_data , y1_dc , y2_rpm , y30_Tm , y31_Tc , y4_volt , y5_current, start_time = NewArrays()
        csv_Data_logger(time_data , y1_dc , y2_rpm , y30_Tm , y31_Tc , y4_volt , y5_current)
    
    # Returns the changes in the graph
    return line1_dc ,line2_rpm, line30_Tm,line31_Tc, line4_volt, line5_current,


#=================================================== MAIN ===================================================#
time_data , y1_dc , y2_rpm , y30_Tm , y31_Tc , y4_volt , y5_current, start_time = NewArrays()

fig, ax1_dc, ax2_rpm, ax3_temp , ax4_volt, ax5_current, titl, line1_dc, line2_rpm, line30_Tm,line31_Tc, line4_volt, line5_current = create_figure()
fig.suptitle(t="Powertrain: Performance Monitor", fontsize=10,backgroundcolor='red',fontweight='bold')
frame_times = np.zeros(MAX_FRAMES)


#plot animation , Interval is in ms
ani = FuncAnimation(fig, update_plot, interval=0, fargs=(frame_times,), repeat=True, frames=list(range(MAX_FRAMES)), blit=True)
plt.show()

# When the Animation is closed, saves all arrays in a .csv
csv_Data_logger(time_data, y1_dc, y2_rpm, y30_Tm, y31_Tc, y4_volt, y5_current)