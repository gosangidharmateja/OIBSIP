# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/gosan/Downloads/dataset/AB_NYC_2019.csv")

print(df.head())

# %%
pd.set_option('display.max_columns', None)


# %%
print("\nShape of Dataset:")
print(df.shape)



# %%
print("\nDataset Information:")
print(df.info())

# %%
print("\nStatistical Summary:")
print(df.describe())

# %%
print("\nColumn Names:")
print(df.columns)


# %%
print("\nMissing Values:")
print(df.isnull().sum())


# %%
plt.figure(figsize=(12,6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

# %%
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)

# %%
df.dropna(subset=['host_name', 'name'], inplace=True)
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# %%
print("\nDuplicate Rows:")
print(df.duplicated().sum())


# %%
df.drop_duplicates(inplace=True)

print("Duplicates Removed Successfully")

# %%
text_columns = ['name', 'host_name', 'neighbourhood_group', 'neighbourhood', 'room_type']

for col in text_columns:
    df[col] = df[col].str.lower().str.strip()

print("\nText Standardization Completed")

# %%
df['last_review'] = pd.to_datetime(df['last_review'])

print("\nDate Conversion Completed")


# %%
numerical_cols = ['price', 'minimum_nights', 'number_of_reviews',
                  'reviews_per_month', 'calculated_host_listings_count',
                  'availability_365']

for col in numerical_cols:
    plt.figure(figsize=(8,4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()

# %%
for col in ['price', 'minimum_nights']:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower_bound) &
            (df[col] <= upper_bound)]

print("\nOutliers Removed")

# %%
plt.figure(figsize=(8,5))
sns.countplot(x='room_type', data=df)
plt.title('Room Type Distribution')
plt.xticks(rotation=45)
plt.show()

# %%
plt.figure(figsize=(10,5))
sns.histplot(df['price'], bins=50, kde=True)
plt.title('Price Distribution')
plt.show()

# %%
plt.figure(figsize=(8,5))
sns.countplot(x='neighbourhood_group', data=df)
plt.title('Neighbourhood Group Distribution')
plt.show()

# %%
top_reviewed = df.sort_values(by='number_of_reviews', ascending=False).head(10)

plt.figure(figsize=(12,5))
sns.barplot(x='number_of_reviews', y='name', data=top_reviewed)
plt.title('Top 10 Most Reviewed Listings')
plt.show()

# %%
plt.figure(figsize=(10,6))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap='coolwarm'
)

plt.title('Correlation Heatmap')
plt.show()

# %%
avg_price = df.groupby('room_type')['price'].mean()

print("\nAverage Price by Room Type:")
print(avg_price)

# Average availability by neighbourhood group
availability = df.groupby('neighbourhood_group')['availability_365'].mean()

print("\nAverage Availability by Neighbourhood Group:")
print(availability)

# Most expensive neighbourhoods
expensive_areas = df.groupby('neighbourhood')['price'].mean().sort_values(ascending=False).head(10)

print("\nTop 10 Expensive Neighbourhoods:")
print(expensive_areas)

# %%
def price_category(price):

    if price < 100:
        return 'Budget'

    elif price < 250:
        return 'Medium'

    else:
        return 'Luxury'

df['price_category'] = df['price'].apply(price_category)

print("\nFeature Engineering Completed")

# %%
plt.figure(figsize=(7,5))

sns.countplot(x='price_category', data=df)

plt.title('Price Category Distribution')
plt.show()

# %%
df.to_csv('cleaned_AB_NYC_2019.csv', index=False)

print("\nCleaned Dataset Saved Successfully")

# %%
print("\nFinal Dataset Shape:")
print(df.shape)

# %%
print("\nFinal Cleaned Dataset:")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df.head()


