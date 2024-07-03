#=================================================== CSV DATA LOGGER ===================================================#
 # Capibarib E-racing
 # Federal University of Pernambuco (UFPE)
 # Group Area: Powertrain
 
 # This file contains the code for the data logger of the monitoring system
 # it just saves the np arrays in a .csv file
import csv

def csv_Data_logger(time_data, y1_dc, y2_rpm, y3_temp_motor, y31_Tc, y4_volt, y5_current):
    HEADER = ['Time', 'DC', 'RPM','Supply_Voltage','Current', 'Temp_motor', 'Temp_controller']
    
    #Save data in a .csv file
    with open('Software/Telemetry-Systems/Motor_Telemetry/Powertrain_Monitor/CSV_Folder/MOTOR_DATA.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        
        # Saves every array as a column
        for time_ms, dc, rpm, temp_motor, temp_ctrl, volt, current in zip(time_data, y1_dc, y2_rpm, y3_temp_motor, y31_Tc, y4_volt, y5_current):
            writer.writerow([time_ms,dc, rpm, temp_motor, temp_ctrl, volt,current])
    # Done!
    print('[Telemetry Data Logger]: Data saved!, you have [',len(time_data),'] Logs!')