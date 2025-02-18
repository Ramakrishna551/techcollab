import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,1)
y1=2*x+5
y2=3*x+10

#create two or more plots in a figure 
plt.subplot(2,1,1)
#plotting the points
plt.plot(x,y1)
plt.title("Graph1")
plt.subplot(2,1,2)
plt.plot(x,y2)
plt.title("Graph2")
print(plt.show())