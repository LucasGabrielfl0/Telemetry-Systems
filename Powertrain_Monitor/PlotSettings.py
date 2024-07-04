from matplotlib import pyplot as plt

DC_MAX      = 100
RPM_MAX     = 10000

XLIM_MAX    = 200
LINE_WEIGTH = 2

MAX_FRAMES = 2000



#=================================================== LINE/FIGURE SETTINGS ===================================================#
# Create Figure, Axys and Lines
def create_figure():
    
    plt.rcParams["figure.figsize"] = (12, 4)

    # Define the layout using subplot2grid
    fig = plt.figure(figsize=(12, 6), tight_layout=True)
    ax1_dc      = plt.subplot2grid((3, 3), (0, 0), colspan=2)
    ax2_rpm     = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)
    ax3_temp    = plt.subplot2grid((3, 3), (0, 2))  
    ax4_volt    = plt.subplot2grid((3, 3), (1, 2))  
    ax5_current = plt.subplot2grid((3, 3), (2, 2)) 
    
    # Lines
    line1_dc,       = ax1_dc.plot([], [],       lw=LINE_WEIGTH, label='DC')
    line2_rpm,      = ax2_rpm.plot([], [],      lw=LINE_WEIGTH, label='RPM')
    line30_Tm,      = ax3_temp.plot([], [],     lw=LINE_WEIGTH, label='Tm')
    line31_Tc,      = ax3_temp.plot([], [],     lw=LINE_WEIGTH, label='Tc')
    line4_volt,     = ax4_volt.plot([], [],     lw=LINE_WEIGTH, label='Supply Voltage')
    line5_current,  = ax5_current.plot([], [],  lw=LINE_WEIGTH, label='Current')

    # Title
    titl = ax1_dc.set_title('Left Plot Title')
    
    # Graph 1: DC
    ax1_dc.set_ylim(0, DC_MAX)
    ax1_dc.set_xlim(0,XLIM_MAX)
    ax1_dc.set_title('DutyCycle')
    ax1_dc.set_ylabel('Percentage [%]')
    ax1_dc.grid(True)

    # Graph 2: RPM
    ax2_rpm.set_ylim(0, RPM_MAX)
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

    return (fig, ax1_dc, ax2_rpm, ax3_temp , ax4_volt, ax5_current, titl, line1_dc, line2_rpm, line30_Tm,line31_Tc, line4_volt, line5_current)
