import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('updated_dataset-iris.csv')

# Scatter Plot of Original Features
sns.pairplot(df, hue='class', vars=['sepal length', 'sepal width', 'petal length', 'petal width'])
plt.suptitle('Scatter Plot of Original Features by Iris Species', y=1.02)

plt.savefig('visualization/scatter_plot_original_features.png')
plt.show()
