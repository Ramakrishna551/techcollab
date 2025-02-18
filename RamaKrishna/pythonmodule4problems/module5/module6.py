import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
#define the dataset 
x=np.arange(0,10,0.1)
y=2*x+5
#plot the datapoint
plt.plot(x,y)
#customise the line plot 

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot Demo")
print(plt.show())