import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
#define the dataset 
x=np.arange(0,10,1)
y=2*x+5
#plot the datapoint
#customise the line plot 
plt.plot(x,y,linewidth=2.0,linestyle=":",color='r',alpha=0.5,marker='o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(['line1'],loc='best')
plt.title("Line Plot Demo")
plt.grid(True)
#change the figue size 
fig=plt.figure(figsize=(10,5))
print(plt.show())