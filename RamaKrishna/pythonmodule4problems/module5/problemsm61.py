import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data (Replace this with actual data)
import pandas as pd
data = {'Contract': ['Month-to-month', 'One year', 'Two year', 'Month-to-month', 'Two year', 'One year', 'Month-to-month']}
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(8, 5))
sns.countplot(x=df['Contract'], color='orange')

# Labels and Title
plt.xlabel('Contract Type of customer')
plt.ylabel('Count')
plt.title('Distribution of Contract')

# Show the plot
plt.show()
