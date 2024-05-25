# Code used for the Dashboard
# Plots live values

# Data Graphs:
# 1. Dc PWM                             } Voltage Control
# 2. RPM                                } Voltage Control

# 3. Input Voltage + Voltage Limit      }
# 4. Current + Current Limit            }

# 5. Temp Motor + Temp Controller       } Temperature

import matplotlib.pyplot as plt                     # Library for Plot
from matplotlib.animation import FuncAnimation      # Library for live plot (Animation)

import matplotx                                     # Library to change theme
plt.style.use(matplotx.styles.dracula)              # Changing theme

import random

Dc_pwm_Data=[]
Velocity_Data=[]

Input_Voltage_Data=[]
Input_Current_Data=[]

Temp_Controller_Data=[]
Temp_Motor_Data=[]

sensor2=[]
time_data=[]

start_time =0





def read_data():
    # Read from serial
    Dc_pwm=random.randint(0, 1)    
    Velocity_Motor =random.randint(0, 100)

    #Input_Voltage =random.randint(0, 100)
    #Input_Current =random.randint(0, 100)
#
    #Temp_Controller =random.randint(0, 100)
    #Temp_Motor =random.randint(0, 100)
#
    ## TimeStamp
    time_current = len(Velocity_Data)


    #====================== Append in the array ======================#
    # Duty Cycle and RPM
    Dc_pwm_Data.append(Dc_pwm)
    Velocity_Data.append(Velocity_Motor)
    
    # Voltage and Current
    #Input_Voltage_Data.append(Input_Voltage)
    #Input_Current_Data.append(Input_Current)
#
    ## Temperature
    #Temp_Controller_Data.append(Temp_Controller)
    #Temp_Motor_Data.append(Temp_Motor)
    #
    
    time_data.append(time_current)

    print("Time: ",time_current, "Data: ",Velocity_Motor)


def update_plot(frame):
    read_data()
    
    plt.cla()
#    plt.plot(time_data, Velocity_Data, label='Motor Velociy')
    g1_rpm.plot(time_data, Velocity_Data,label='Motor Velociy')
    g2_dc.plot(time_data, Dc_pwm_Data,label='Dc')
    
    #a1_rpm.plot(time_data, Velocity_Data,label='Motor Velociy')
    #a2_dc.plot(time_data, Dc_pwm_Data,label='Dc')
    #a3_current.plot(time_data, Velocity_Data,label='Motor Velociy')
    #a4_Temp.plot(time_data, Dc_pwm_Data,label='Dc')

    fig.tight_layout

    plt.xlabel('Time')
    plt.ylabel('Velocity [RPM]')
    
    plt.legend()
    plt.grid()


#fig, (a1_rpm, a2_dc, a3_current, a4_Temp)= plt.subplots()
fig, (g1_rpm, g2_dc)= plt.subplots(2,1, gridspec_kw={'height_ratios': [1, 3]})

#fig, (a1_rpm, a2_dc, a3_current, a4_Temp)= plt.subplots(2,1, gridspec_kw={'height_ratios': [1, 3]})

fig.suptitle("Motor Monitoring System")
ani=FuncAnimation(fig=fig, func=update_plot, interval=100)


plt.show()


