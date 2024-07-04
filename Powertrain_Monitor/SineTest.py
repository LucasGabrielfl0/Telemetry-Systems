import numpy as np

def NewArraysTest():
    start_time= 0
    time_array=np.zeros(0,float)
    y1=np.zeros(0,float)
    y2=np.zeros(0,float)
    y3=np.zeros(0,float)
    y4=np.zeros(0,float)
    y5=np.zeros(0,float)
    y6=np.zeros(0,float)

    return time_array, y1, y2, y3, y4 , y5, y6 , start_time




def ReadTest(time_c,time_data, y1_dc, y2_rpm, y30_Tm, y31_Tc, y4_volt, y5_current):
    value=500*np.sin((100 / (10*2** 10)) * 2 * np.pi * time_c) + 500

    y1_dc       =   np.append(y1_dc, value)
    y2_rpm      =   np.append(y2_rpm, value*5)
    y30_Tm      =   np.append(y30_Tm, value*0.1)
    y31_Tc      =   np.append(y31_Tc, value*0.05)
    y4_volt     =   np.append(y4_volt, value*0.1)
    y5_current  =   np.append(y5_current, value*0.2)

    time_data=np.append(time_data, time_c)
    time_c= time_c+1

    # Returns all arrays
    return time_c, time_data, y1_dc, y2_rpm, y30_Tm, y31_Tc, y4_volt, y5_current
