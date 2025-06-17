Q1 = df['Score'].quantile(0.25)
Q3 = df['Score'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers_iqr = df[(df['Score'] < lower_bound) | (df['Score'] > upper_bound)]
print("IQR Outliers:\n", outliers_iqr)
