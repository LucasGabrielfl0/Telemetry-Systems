#=================================================== DRAFT CODE ===================================================#
# Code to test the serial read in python
import serial
import numpy as np
import re
import time
#=========================================== COMMUNICATION SETUP ===========================================#
PC_PORT = 'COM7'
BAUD_RATE = 9600

ser= serial.Serial(PC_PORT, BAUD_RATE)


#=================================================== PLOT SETUP ===================================================#
# Empty Arrays of data
y1_dc       = np.zeros(0,float)
y2_rpm      = np.zeros(0,float)
y31_temp_m  = np.zeros(0,float)
y32_temp_c  = np.zeros(0,float)
y4_volt     = np.zeros(0,float)
y5_current  = np.zeros(0,float)
time_data   = np.zeros(0,float)



def read_Serial():
    global y1_dc, y2_rpm, y31_temp_m, y32_temp_c, y4_volt, y5_current, time_data
    
    # Read Serial Data
    Stm32_Data= ser.readline().decode('utf8')
    print(Stm32_Data) 
    
    # Get only the numbers from serial data
    # Data_Array=re.findall(r'\d+', Stm32_Data)

    # # Get Current Values for each variable
    # dc_c        = float(Data_Array[3])
    # rpm_c       = float(Data_Array[4])
    # temp_m_c    = float(Data_Array[5])
    # temp_c_c    = float(Data_Array[6])
    # volt_c      = float(Data_Array[7])
    # current_c   = float(Data_Array[8])
    
    # # Add the current value to the Data array
    # y1_dc       = np.append(y1_dc       , dc_c)
    # y2_rpm      = np.append(y2_rpm      , rpm_c)
    # y31_temp_m  = np.append(y31_temp_m  , temp_m_c)
    # y32_temp_c  = np.append(y32_temp_c  , temp_c_c)
    # y4_volt     = np.append(y4_volt     , volt_c)
    # y5_current  = np.append(y5_current  , current_c)
    # time_data   = np.append(time_data   , time_c)



while True:
    read_Serial()
    # time.sleep(1)
#=========================================== COMMUNICATION SETUP ===========================================#






#=========================================== COMMUNICATION SETUP ===========================================#


