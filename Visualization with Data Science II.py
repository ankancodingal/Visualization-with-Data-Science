# Make a time Velocity Line Graph
import matplotlib.pyplot as plt
x=[0,5,10,15,20,25,30]
y1=[10,15,20,20,30,15,0]
y2=[10,12,15,12,20,10,0]
plt.plot(x,y1,linestyle='dashed',marker='D')
plt.plot(x,y2,linestyle='dashed',marker='D')
plt.title('velocity-Time Graph')
plt.xlabel('Velocity m/s')
plt.ylabel('Time(s)')
plt.xlim(5,25)
plt.ylim(5,25)
plt.legend()
plt.show()

# Solve the equation
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,11,1)
y1=(2*x)+1
y2=(2*x*x)+2
plt.plot(x,y1,'g',linewidth=3,label='y=2x+1')
plt.plot(x,y2,'r',linewidth=3,label='y=2x^2+2')
plt.legend()
plt.show()
