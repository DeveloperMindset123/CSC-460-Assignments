import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('updated_dataset-iris.csv')

# Plotting Petal Ratio Distribution
plt.figure(figsize=(6, 6))
sns.boxplot(x='class', y='Petal Ratio', data=df)
plt.title('Petal Ratio Distribution by Iris Species')
plt.xlabel('Species')
plt.ylabel('Petal Ratio')

plt.savefig('visualization/petal_ratio_distribution.png')
plt.show()

