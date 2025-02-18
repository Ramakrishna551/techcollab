import matplotlib.pyplot as plt
numbers=[10,12,16,19,11,20,26,28,30,38,35,34,60,68,64,62,70,78,79,85,94,95]
#creating histogram
plt.hist(numbers,bins=[0,20,40,60,80])
print(plt.show())