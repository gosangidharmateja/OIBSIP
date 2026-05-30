# %%
#import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %%
# Load dataset

df = pd.read_csv("menu.csv")

# %%
# Display first 5 rows

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)

print(df.head())

# %%
print(df.shape)


# %%
#dataset information

print(df.info())

# %%
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)
print(df.describe())

# %%
#checking null values

print(df.isnull().sum())

# %%
#checking duplicate values

print(df.duplicated().sum())

# %%
#calories distribution

plt.figure(figsize=(10,5))
sns.histplot(df['Calories'], bins=30, kde=True)
plt.title('Distribution of Calories')
plt.show()

# %%
#calories category

avg_calories = df.groupby('Category')['Calories'].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
avg_calories.plot(kind='bar')
plt.title('Average Calories by Category')
plt.ylabel('Calories')
plt.show()

# %%
#calories vs fats

plt.figure(figsize=(8,6))
sns.scatterplot(x='Total Fat', y='Calories', data=df)
plt.title('Calories vs Total Fat')
plt.show()

# %%
#calories vs protein

plt.figure(figsize=(8,6))
sns.scatterplot(x='Protein', y='Calories', data=df)
plt.title('Calories vs Protein')
plt.show()

# %%
#correlation heatmap

plt.figure(figsize=(14,10))
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# %%
#protin category

protein_category = df.groupby('Category')['Protein'].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
protein_category.plot(kind='bar', color='green')
plt.title('Average Protein by Category')
plt.ylabel('Protein')
plt.show()

# %%
#sodium category

plt.figure(figsize=(12,6))
sodium_category = df.groupby('Category')['Sodium'].mean().sort_values(ascending=False)
sodium_category.plot(kind='bar', color='red')
plt.title('Average Sodium by Category')
plt.ylabel('Sodium')
plt.show()

# %%
# Boxplot
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Calories'])
plt.title('Boxplot of Calories')
plt.show()

# %%



