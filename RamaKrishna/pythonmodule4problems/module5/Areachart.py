import matplotlib.pyplot as plt
#define the data set 
x=range(1,15)
y=[1,4,6,8,4,5,3,2,4,1,5,6,8,7]
#creating the area plot 
#customise the plot 
plt.stackplot(x,y,colors='g',alpha=0.5)
plt.grid(True)
print(plt.show())