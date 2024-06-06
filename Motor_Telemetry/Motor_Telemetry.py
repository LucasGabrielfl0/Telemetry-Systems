#=================================================== MOTOR TELEMETRY SYSTEM ===================================================#
 # Capibarib E-racing
 # Federal University of Pernambuco (UFPE)
 # Group Area: Powertrain
 
 # This file contains the Motor/Controller Telemetry system [Monitoring Interface] for tests in the Laboratory.
 # Details of the Physical connections and the circuit can be found on the Github or the Team's Google Drive
 
# This interface has 2 distinct Modes: USB_READ and RS232_READ


#=================================================== LIBRARIES ===================================================#
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation          # Animation
import matplotx                                         # Library to change theme []
import numpy as np
import time
import serial

plt.style.use(matplotx.styles.dracula)

#=================================================== COMMUNICATION SETUP =================================================#
PC_PORT = 'COM7'
BAUD_RATE = 9600
ser= serial.Serial(PC_PORT, BAUD_RATE)


#=================================================== GRAPH SETUP ===================================================#
plt.rcParams["figure.figsize"] = (12, 4)

N = 2 ** 10
line_width = 2
# axRxlims = [0, N]
# axRylims = [0, 160]

dframe = np.full(N + 1, fill_value=np.nan, dtype=float)  # Use float directly
fig, ax_1 = plt.subplots(figsize=(6, 4), tight_layout=True)

time_data =[]
RPM_data  =[]


#=================================================== FUNCTIONS ===================================================#

#------------------------------------------------- Read Data from Serial port --------------------------------#
def read_Serial():
    Stm32_Data= ser.readline().decode('ascii')
    print(Stm32_Data)


#------------------------------------------------- Generate de Axys data --------------------------------------#
def create_figure():
    line_1, = ax_1.plot([], [], lw=line_width, label='Left Line')    #
    title_1 = ax_1.set_title('Left Plot Title')                      # Set Tittle

    ax_1.set_xlabel("Time [ms]")                                    #
    ax_1.set_ylabel("Voltage [V]")                                  #
    ax_1.grid(True)                                                 #

    return (fig, ax_1, title_1, line_1)


#------------------------------------------------- Saves Data in a .csv file ----------------------------------#
def Save_CSV():
    pass



#------------------------------------------------- Updates Plot ----------------------------------------------#
def update_plot(frame, frame_times):
    
    # Save_CSV()                                              # 
    frame_times[frame] = time.perf_counter()                # Time in s
    linel.set_data(time_data[frame], RPM_data[frame])       # Add new points to graph
    
    # Dont Rescale unless the data is out of the graph's bounds
    rescale = False
    if RPM_data[frame, frame] < ax_1.get_ylim()[0]:
        ax_1.set_ylim(RPM_data[frame, frame] - 0.1, ax_1.get_ylim()[1])
        rescale = True
    if RPM_data[frame, frame] > ax_1.get_ylim()[1]:
        ax_1.set_ylim(ax_1.get_ylim()[0], RPM_data[frame, frame] + 0.1)
        rescale = True
    if time_data[frame, frame] > ax_1.get_xlim()[1]:
        ax_1.set_xlim(ax_1.get_xlim()[0], ax_1.get_xlim()[1] + N / 5)
        rescale = True
    if frame == len(time_data) - 1:
        rescale = True
    
    if rescale:
        fig.canvas.draw()   # Redraws the graph if there were changes
    
    # Return the changes in the graph
    return linel, titl


#=================================================== MAIN ===================================================#
fig, ax_1, titl, linel = create_figure()
fig.suptitle(t="NOVA 15 Motor Interface", fontsize='large')
frame_times = np.zeros(N)


ani = FuncAnimation(fig, update_plot, interval=0, fargs=(frame_times,), repeat=False, frames=list(range(N)), blit=True)
plt.show()
