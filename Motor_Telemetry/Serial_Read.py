#=================================================== DRAFT CODE ===================================================#
# Code to test the serial read in python
import serial

#=========================================== COMMUNICATION SETUP ===========================================#
PC_PORT = 'COM7'
BAUD_RATE = 9600
# fileName="Motor_Data.csv"
# samples= 3000


ser= serial.Serial(PC_PORT, BAUD_RATE)


while True:
    Stm32_Data= ser.readline().decode('ascii')
    print(Stm32_Data)

#=========================================== COMMUNICATION SETUP ===========================================#






#=========================================== COMMUNICATION SETUP ===========================================#


