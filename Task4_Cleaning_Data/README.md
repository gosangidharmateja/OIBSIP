# Airbnb NYC 2019 Data Cleaning & Analysis Project

## Project Overview

This project focuses on cleaning, preprocessing, and analyzing the Airbnb NYC 2019 dataset using Python. The main objective is to improve data quality and generate meaningful business insights through Exploratory Data Analysis (EDA).

Data cleaning is one of the most important steps in data analytics because poor-quality data leads to inaccurate analysis and unreliable decision-making.

---

# Dataset Information

- Dataset Name: AB_NYC_2019.csv
- Dataset Source: Airbnb NYC 2019 Listings
- Records: 48,000+ Airbnb listings
- File Format: CSV

---

# Project Objectives

The goals of this project are:

- Handle missing values
- Remove duplicate records
- Standardize inconsistent data
- Detect and remove outliers
- Perform exploratory data analysis
- Generate business insights
- Export cleaned dataset

---

# Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python | Programming Language |
| Pandas | Data Cleaning & Manipulation |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Jupyter Notebook | Project Development |

---

# Project Workflow

## 1. Data Collection

The dataset was loaded using Pandas.

```python
import pandas as pd

df = pd.read_csv('AB_NYC_2019.csv')
```

---

## 2. Data Exploration

Basic dataset exploration was performed to understand:

- Dataset dimensions
- Data types
- Missing values
- Statistical summary

```python
df.info()
df.describe()
```

---

## 3. Missing Value Handling

### Missing Values Found

| Column | Missing Values |
|---|---|
| last_review | 6687 |
| reviews_per_month | Some values |

### Cleaning Performed

- `reviews_per_month` missing values were filled with `0`
- Missing values in `last_review` were retained because they indicate listings with no reviews

```python
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
```

---

## 4. Duplicate Removal

Duplicate records were identified and removed.

```python
df.drop_duplicates(inplace=True)
```

---

## 5. Data Standardization

Text columns were standardized by:

- converting text to lowercase
- removing extra spaces

```python
df['host_name'] = df['host_name'].str.lower().str.strip()
```

---

## 6. Date Conversion

The `last_review` column was converted into datetime format.

```python
df['last_review'] = pd.to_datetime(df['last_review'])
```

---

## 7. Outlier Detection & Removal

Outliers were detected using the IQR (Interquartile Range) method.

### Formula

```text
IQR = Q3 - Q1
```

Outliers were removed from:
- price
- minimum_nights

---

## 8. Exploratory Data Analysis (EDA)

Several visualizations were created:

- Room Type Distribution
- Price Distribution
- Correlation Heatmap
- Top Reviewed Listings
- Neighbourhood Analysis

---

# Key Insights

## Room Types

- Entire home/apartment listings were the most common.
- Private rooms were also highly available.

## Pricing

- Most listings were budget-friendly.
- Some luxury listings created extreme outliers.

## Reviews

- Listings with higher availability generally received more reviews.

## Neighbourhoods

- Manhattan had the highest average prices.
- Brooklyn had the largest number of listings.

---

# Feature Engineering

A new feature called `price_category` was created.

| Price Range | Category |
|---|---|
| < 100 | Budget |
| 100 - 250 | Medium |
| > 250 | Luxury |

```python
def price_category(price):

    if price < 100:
        return 'Budget'

    elif price < 250:
        return 'Medium'

    else:
        return 'Luxury'
```

---

# Final Dataset

The cleaned dataset was exported as:

```text
cleaned_AB_NYC_2019.csv
```

```python
df.to_csv('cleaned_AB_NYC_2019.csv', index=False)
```

---

# Folder Structure

```text
Airbnb-NYC-Data-Cleaning-Project/
│
├── data/
│   ├── AB_NYC_2019.csv
│   └── cleaned_AB_NYC_2019.csv
│
├── notebooks/
│   └── airbnb_data_cleaning.ipynb
│
├── images/
│   └── visualizations/
│
├── README.md
│
└── requirements.txt
```

---

# Business Value

This project demonstrates practical data analytics skills including:

- Data preprocessing
- Data quality improvement
- Missing value handling
- Outlier treatment
- Data visualization
- Business insight generation

These skills are highly valuable in:
- Data Analytics
- Data Science
- Business Intelligence
- Machine Learning projects

---

# Challenges Faced

- Handling missing review dates
- Managing extreme price outliers
- Standardizing text data
- Choosing appropriate cleaning methods

---

# Future Improvements

Possible future enhancements:

- Build Power BI Dashboard
- Add Machine Learning Models
- Create Interactive Streamlit App
- Deploy Project Online
- Add Geospatial Visualizations

---

# Conclusion

This project successfully cleaned and analyzed the Airbnb NYC 2019 dataset. Through proper data preprocessing and visualization techniques, meaningful business insights were generated from messy real-world data.

The project demonstrates strong foundational skills in data cleaning, exploratory data analysis, and business analytics using Python.

---
