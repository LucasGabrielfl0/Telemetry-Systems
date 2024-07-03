import numpy as np

def NewArraysTest():
    time_cons= 0
    time_array=np.zeros(0,float)
    y1=np.zeros(0,float)
    y2=np.zeros(0,float)
    y3=np.zeros(0,float)
    y4=np.zeros(0,float)
    y5=np.zeros(0,float)
    y6=np.zeros(0,float)

    return time_array, y1, y2, y3, y4 , y5, y6, y6 , time_cons




def ReadTest(time_data, y1_dc, y2_rpm, y30_Tm, y31_Tc, y4_volt, y5_current, y , time_c):
    value=500*np.sin((100 / (10*2** 10)) * 2 * np.pi * time_c) + 500
    y=np.append(y, value)
    y1_dc=y
    y2_rpm=y*5
    y30_Tm=y*0.1
    y31_Tc=y*0.05
    y4_volt=y*0.1
    y5_current=y*0.2

    time_data=np.append(time_data, time_c)
    time_c= time_c+1

    # Returns all arrays
    return time_data, y1_dc, y2_rpm, y30_Tm, y31_Tc, y4_volt, y5_current, y , time_c
