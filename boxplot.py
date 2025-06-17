

import pandas as pd

import matplotlib.pyplot as plt

# Sample data with an outlier
data = {'Score': [70, 75, 80, 85, 90, 100, 300]}
df = pd.DataFrame(data)

# Boxplot
plt.boxplot(df['Score'])
plt.title("Boxplot for Score")
plt.ylabel("Score")
plt.show()

input("Press Enter to exit...")


