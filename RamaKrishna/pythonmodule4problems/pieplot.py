import matplotlib.pyplot as plt
#preparing the dataset
label= ['Dog','Cat','Wolf','Lion']
sizes=[50,48,60,80]
#creating pie chart 
#customization 
plt.pie(sizes, labels=label,autopct='%1.1f%%',shadow=True,startangle=90) 

plt.title("Pie Plot Demo")
print(plt.show())

