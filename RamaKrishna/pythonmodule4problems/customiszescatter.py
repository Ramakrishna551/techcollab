import matplotlib.pyplot as plt
#creating dataset 
a=[10,20,30,40,50,60,70,80]
b=[5,3,2,5,6,1,4,2]
x=[1,2,3,4,3,2,1,2]
#creating scatter plot 
plt.scatter(a,b, c='g',s=200,edgecolors='y',marker='o',alpha=0.5)

plt.scatter(a,x,c='r',s=400,edgecolors='b',marker='4',alpha=1)
plt.legend(['b','x'],loc='best')
plt.title("Scatter Plot Demo")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
print(plt.show())
