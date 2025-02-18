import matplotlib.pyplot as plt
import numpy as np
#creating a dataset
data={'Apples':20,'Mangoes':15,'Lemon':30,'Oranges':10}
names =list(data.keys())
values=list(data.values())

fig = plt.figure(figsize=(10,5))
#creating  the bar plot 

plt.bar(names,values)
print(plt.show())