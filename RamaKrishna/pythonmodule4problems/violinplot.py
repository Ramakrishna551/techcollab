import matplotlib.pyplot as plt
#data preparation
total=[20,4,1,30,20,10,20,70,30,10]
order=[10,13,1,15,17,2,30,44,2,1]
discount=[30,10,20,50,10,20,50,60,20,45,85]
data = list([total,order,discount])
#plotting the data 
plt.violinplot(data,showmeans=True,showmedians=True)
plt.title("Violin Plot Demo")
plt.grid(True)
print(plt.show())