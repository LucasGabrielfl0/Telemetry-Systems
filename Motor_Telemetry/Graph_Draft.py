# static Draft of how the graph will look like
# Just visual a thing
import matplotlib.pyplot as plt
import numpy as np
import matplotx                                         # Library to change theme []
plt.style.use(matplotx.styles.dracula)

# Create the figure and subplots
fig = plt.figure(figsize=(12, 6))

# Define the layout using subplot2grid
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)  # ax1 at position (0, 0)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)  # ax2 at position (1, 0)
ax3 = plt.subplot2grid((3, 3), (0, 2))  # ax3 at position (0, 1)
ax4 = plt.subplot2grid((3, 3), (1, 2))  # ax4 at position (1, 1)
ax5 = plt.subplot2grid((3, 3), (2, 2))  # ax4 at position (1, 1)

# Generate some sample data
x = np.linspace(0, 500, 3000)
y0 = 500*np.sin(x/100) + 500
y1 = 50*np.sin(x/100) +50
y2 = 5000*np.cos(x/100) + 5000
y3 = np.tan(x/100)
y4 = np.exp(x/100)
y5 = np.log(x/100 + 1)

# Plot on each subplot
ax1.plot(x, y0, color='red')
ax1.set_ylim(0, 1000)
ax1.set_title('DutyCycle')
ax1.grid(True)
ax1.set_ylabel('Percentage [%]')
# ax1.set_xlabel('time [ms]')


ax2.plot(x, y2, color='green')
ax2.set_title('Wheel Velocity')
ax2.grid(True)
ax2.set_ylim(0, 10000)
ax2.set_ylabel('Velocuty [RPM]')
ax2.set_xlabel('time [ms]')

ax3.plot(x, y3,x, y4,label=['a', 'aaaaaaaaa'])
ax3.set_title('Temperature: Motor | Motor Controller')
ax3.grid(True)
ax3.set_ylim(0, 150)
ax3.set_ylabel('Temperaure [°C]')
# ax3.set_xlabel('time [ms]')


ax4.plot(x, y4)
ax4.set_title('Supply Voltage')
ax4.set_ylim(0, 400)
ax4.grid(True) 
ax4.set_ylabel('Voltage [V]')
# ax4.set_xlabel('time [ms]')

ax5.plot(x, y1)
ax5.set_title('Phase Current')
ax5.grid(True) 
ax5.set_ylim(0, 256)
ax5.set_ylabel('Current [A]')
ax5.set_xlabel('time [ms]')

# Adjust layout
plt.tight_layout()
fig.suptitle(t="Powertrain", fontsize=10,backgroundcolor='red',fontweight='bold')
# Show the plot

plt.show()
