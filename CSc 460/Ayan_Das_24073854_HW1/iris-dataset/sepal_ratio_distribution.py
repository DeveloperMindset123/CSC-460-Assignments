import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('updated_dataset-iris.csv')

# Plotting Sepal Ratio Distribution
plt.figure(figsize=(6, 6))
sns.boxplot(x='class', y='Sepal Ratio', data=df)
plt.title('Sepal Ratio Distribution by Iris Species')
plt.xlabel('Species')
plt.ylabel('Sepal Ratio')

plt.savefig('visualization/sepal_ratio_distribution.png')
plt.show()
