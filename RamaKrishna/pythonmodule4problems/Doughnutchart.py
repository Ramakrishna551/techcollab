import matplotlib.pyplot as plt


groupnames =["Group1","Group2","Group3"]
groupsize=[20,30,40]
sizecentre=[4]

#cresting doughnut chart
pie1=plt.pie(groupsize,labels=groupnames,radius=1.4)
pie2=plt.pie(sizecentre,radius=1.0,colors='w')
print(plt.show())