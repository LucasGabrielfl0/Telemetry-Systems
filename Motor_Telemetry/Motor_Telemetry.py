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
import numpy as np
import time
import serial
import re
import csv

plt.style.use(matplotx.styles.dracula)

#=================================================== COMMUNICATION SETUP =================================================#
PC_PORT = 'COM7'
BAUD_RATE = 9600
ser= serial.Serial(PC_PORT, BAUD_RATE)

# Empty Arrays of data
y1_dc       = np.zeros(0,float)
y2_rpm      = np.zeros(0,float)
y30_Tm      = np.zeros(0,float)
y31_Tc      = np.zeros(0,float)
y4_volt     = np.zeros(0,float)
y5_current  = np.zeros(0,float)
time_data   = np.zeros(0,float)

#=================================================== READ SERIAL ===================================================#
# Read Data from serial port and stores it's values in the array
def read_Serial():
    global y1_dc, y2_rpm, y31_temp_m, y32_temp_c, y4_volt, y5_current, time_data
    
    # Read Serial Data
    Stm32_Data= ser.readline().decode('ascii')
    print(Stm32_Data) 
    
    # Get only the numbers from serial data
    Data_Array=re.findall(r'\d+', Stm32_Data)

    # Get Current Values for each variable
    dc_c        = float(Data_Array[3])
    rpm_c       = float(Data_Array[4])
    Tm_c        = float(Data_Array[5])
    Tc_c        = float(Data_Array[6])
    volt_c      = float(Data_Array[7])
    current_c   = float(Data_Array[8])
    
    # Add the current value to the Data array
    y1_dc       = np.append(y1_dc       , dc_c)
    y2_rpm      = np.append(y2_rpm      , rpm_c)
    y30_Tm      = np.append(y30_Tm      , Tm_c)
    y31_Tc      = np.append(y31_Tc      , Tc_c)
    y4_volt     = np.append(y4_volt     , volt_c)
    y5_current  = np.append(y5_current  , current_c)
    # time_data   = np.append(time_data   , time_c)

#=================================================== CSV DATA LOGGER ===================================================#
# saves Data in the .csv file in the specified folder
def csv_Data_logger(time_data, y1_dc, y2_rpm, y3_temp_motor, y31_Tc, y4_volt, y5_current):
    HEADER = ['Time', 'DC', 'RPM','Supply_Voltage','Current', 'Temp_motor', 'Temp_controller']
    
    #Save data in a .csv file
    with open('Software/Telemetry-Systems/Motor_Telemetry/CSV_Folder/MOTOR_DATA.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        
        # Saves every array as a column
        for time_ms, dc, rpm, temp_motor, temp_ctrl, volt, current in zip(time_data, y1_dc, y2_rpm, y3_temp_motor, y31_Tc, y4_volt, y5_current):
            writer.writerow([time_ms,dc, rpm, temp_motor, temp_ctrl, volt,current])
    # Done!
    print('[Telemetry Data Logger]: Data saved!, you have [',len(time_data),'] Logs!')



#=================================================== GRAPH PARAMETERS ===================================================#
RPM_MAX = 10000
XLIM_MAX= 1000
MAX_FRAMES = 2*2 ** 10
LINE_WEIGTH = 2


plt.rcParams["figure.figsize"] = (12, 4)

# Define the layout using subplot2grid
fig = plt.figure(figsize=(12, 6), tight_layout=True)
ax1_dc      = plt.subplot2grid((3, 3), (0, 0), colspan=2)
ax2_rpm     = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)
ax3_temp    = plt.subplot2grid((3, 3), (0, 2))  
ax4_volt    = plt.subplot2grid((3, 3), (1, 2))  
ax5_current = plt.subplot2grid((3, 3), (2, 2)) 


#=================================================== LINE/FIGURE SETTINGS ===================================================#
# Create Figure, Axys and Lines
def create_figure():
    line1_dc,       = ax1_dc.plot([], [],       lw=LINE_WEIGTH, label='DC')
    line2_rpm,      = ax2_rpm.plot([], [],      lw=LINE_WEIGTH, label='RPM')
    line30_Tm,      = ax3_temp.plot([], [],     lw=LINE_WEIGTH, label='Tm')
    line31_Tc,      = ax3_temp.plot([], [],     lw=LINE_WEIGTH, label='Tc')
    line4_volt,     = ax4_volt.plot([], [],     lw=LINE_WEIGTH, label='Supply Voltage')
    line5_current,  = ax5_current.plot([], [],  lw=LINE_WEIGTH, label='Current')

    titl = ax1_dc.set_title('Left Plot Title')
    
    # Graph 1: DC
    ax1_dc.set_ylim(0, 1000)
    ax1_dc.set_xlim(0,XLIM_MAX)
    ax1_dc.set_title('DutyCycle')
    ax1_dc.set_ylabel('Percentage [%]')
    ax1_dc.grid(True)

    # Graph 2: RPM
    ax2_rpm.set_ylim(0, 10000)
    ax2_rpm.set_xlim(0,XLIM_MAX)
    ax2_rpm.set_title('Wheel Velocity')
    ax2_rpm.set_ylabel('Velocuty [RPM]')
    ax2_rpm.set_xlabel('time [ms]')
    ax2_rpm.grid(True)

    # Graph 3: TEMPERATURE
    ax3_temp.set_ylim(0, 150)
    ax3_temp.set_xlim(0,XLIM_MAX)
    ax3_temp.set_title('Temperature: Motor | Motor Controller')
    ax3_temp.set_ylabel('Temperaure [°C]')
    ax3_temp.grid(True)
    ax3_temp.legend([line30_Tm, line31_Tc], ['Motor', 'Controller'], loc="upper left")    

    # Graph 4: SUPLY VOLTAGE
    ax4_volt.set_ylim(0, 400)
    ax4_volt.set_xlim(0,XLIM_MAX)
    ax4_volt.set_title('Supply Voltage')
    ax4_volt.set_ylabel('Voltage [V]')
    ax4_volt.grid(True)

    # Graph 5: PHASE CURRENT
    ax5_current.set_ylim(0, 256)
    ax5_current.set_xlim(0,XLIM_MAX)
    ax5_current.set_title('Phase Current')
    ax5_current.set_ylabel('Current [A]')
    ax5_current.set_xlabel('time [ms]')
    ax5_current.grid(True)

    return (fig, ax1_dc, titl, line1_dc, line2_rpm, line30_Tm,line31_Tc, line4_volt, line5_current)


#================================================ PLOT UPDATE: BLITING + AUTO AXYS ================================================#
# Animated Plot
def update_plot(frame, frame_times):
    global time_data
    global y1_dc, y2_rpm, y30_Tm, y31_Tc, y4_volt, y5_current

    read_Serial()
    frame_times[frame] = time.perf_counter()
    print("Time: ",time_data[frame],"  volt: ",y1_dc[frame])

    time_current=time_data
    line1_dc.set_data(time_current      , y1_dc)
    line2_rpm.set_data(time_current     , y2_rpm)
    line30_Tm.set_data(time_current     , y30_Tm)
    line31_Tc.set_data(time_current     , y31_Tc)
    line4_volt.set_data(time_current    , y4_volt)
    line5_current.set_data(time_current , y5_current)
    
    rescale = False
    
    if y1_dc[frame] < ax1_dc.get_ylim()[0]:
        ax1_dc.set_ylim(y1_dc[frame] - 0.1, ax1_dc.get_ylim()[1])
        rescale = True

    if y1_dc[frame] > ax1_dc.get_ylim()[1]:
        ax1_dc.set_ylim(ax1_dc.get_ylim()[0], y1_dc[frame] + 0.1)
        rescale = True

    #Update Time Axys
    if time_data[frame] > ax1_dc.get_xlim()[1]:
        ax2_rpm.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + MAX_FRAMES / 5)
        ax3_temp.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + MAX_FRAMES / 5)
        ax4_volt.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + MAX_FRAMES / 5)
        ax5_current.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + MAX_FRAMES / 5)
        ax1_dc.set_xlim(ax1_dc.get_xlim()[0], ax1_dc.get_xlim()[1] + MAX_FRAMES / 5)
        rescale = True

    if frame == len(time_data) - 1:
        rescale = True
    
    if rescale:
        fig.canvas.draw()
    
    return line1_dc ,line2_rpm, line30_Tm,line31_Tc, line4_volt, line5_current,


#=================================================== MAIN ===================================================#
fig, ax1_dc, titl, line1_dc ,line2_rpm, line30_Tm,line31_Tc, line4_volt, line5_current = create_figure()
fig.suptitle(t="Powertrain: Performance Monitor", fontsize=10,backgroundcolor='red',fontweight='bold')
frame_times = np.zeros(MAX_FRAMES)


#plot animation
ani = FuncAnimation(fig, update_plot, interval=0, fargs=(frame_times,), repeat=False, frames=list(range(MAX_FRAMES)), blit=True)
plt.show()

# When the Animation is done, saves .csv
csv_Data_logger(time_data, y1_dc, y2_rpm, y30_Tm, y31_Tc, y4_volt, y5_current)
