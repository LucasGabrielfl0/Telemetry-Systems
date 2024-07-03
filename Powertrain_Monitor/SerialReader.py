import numpy as np
import re
import serial

#=========================================== COMMUNICATION SETUP ===========================================#
PC_PORT = 'COM7'
BAUD_RATE = 9600

ser= serial.Serial(PC_PORT, BAUD_RATE)


def ID_confirm(Data_string):
    Id= Data_string.split(":")
    if Id[0] == '[CAN]':
        return True
    else:
        return False


# Create/Resets data arrays
def NewArrays():
    y1          = np.zeros(0,float)
    y2          = np.zeros(0,float)
    y30         = np.zeros(0,float)
    y31         = np.zeros(0,float)
    y4          = np.zeros(0,float)
    y5          = np.zeros(0,float)
    time_data   = np.zeros(0,float)
    
    return time_data, y1, y2, y30, y31, y4, y5




# Read Data from serial port and stores it's values in the array
# message example:'[CAN]: | TIME: 500.12 | PWM= 100.11% |  RPM= 300 | Vs=301.45 V | Ic= 200 A |  Tm= 20 °C | Tc= 21 °C'
def ReadSerial(time_data, y1_dc, y2_rpm, y30_Tm, y31_Tc, y4_volt, y5_current):
    # Keeps reading until finds right msg
    while True:
        Stm32_Data= ser.readline().decode('utf8')   # Read Serial  
        if ID_confirm(Stm32_Data):                  # Confirms if its the CAN msg
            break
        print(Stm32_Data)  

    Data_Array=re.findall(r"[\d.]+", Stm32_Data)    # Get only the numbers from serial data
    print(Data_Array)
    
    # Get Current Values for each variable
    time_c      = float(Data_Array[0])
    dc_c        = float(Data_Array[1])
    rpm_c       = int(Data_Array[2])
    volt_c      = float(Data_Array[3])
    current_c   = int(Data_Array[4])
    Tm_c        = int(Data_Array[5])
    Tc_c        = int(Data_Array[6])

    # Add the current value to the Data array
    time_data   = np.append(time_data   , time_c)
    y1_dc       = np.append(y1_dc       , dc_c)
    y2_rpm      = np.append(y2_rpm      , rpm_c)
    y30_Tm      = np.append(y30_Tm      , Tm_c)
    y31_Tc      = np.append(y31_Tc      , Tc_c)
    y4_volt     = np.append(y4_volt     , volt_c)
    y5_current  = np.append(y5_current  , current_c)

    # Time starts from 0
    start_time  = time_data[0]
    time_data   = time_data - start_time
    
    # Returns all arrays
    return time_data, y1_dc, y2_rpm, y30_Tm, y31_Tc, y4_volt, y5_current

