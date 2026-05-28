
# Exploratory Data Analysis (EDA) Report

## Dataset Overview
This dataset contains menu nutrition information for retail food items.

### Basic Information
- Number of rows: 260
- Number of columns: 24
- Missing values: 0
- Duplicate rows: 0

## Columns
Category, Item, Serving Size, Calories, Calories from Fat, Total Fat, Total Fat (% Daily Value), Saturated Fat, Saturated Fat (% Daily Value), Trans Fat, Cholesterol, Cholesterol (% Daily Value), Sodium, Sodium (% Daily Value), Carbohydrates, Carbohydrates (% Daily Value), Dietary Fiber, Dietary Fiber (% Daily Value), Sugars, Protein, Vitamin A (% Daily Value), Vitamin C (% Daily Value), Calcium (% Daily Value), Iron (% Daily Value)

## Key Findings
1. The dataset contains **9 unique categories**.
2. Average calories across all items: **368.27**.
3. Highest calorie item:
   - **Chicken McNuggets (40 piece)** with **1880 calories**.
4. Lowest calorie item:
   - **Diet Coke (Small)** with **0 calories**.
5. Categories with the highest average calories are mainly large meals and desserts.

## Statistical Summary

### Numerical Features Summary

| Feature | Mean | Median | Min | Max | Std Dev |
|---|---:|---:|---:|---:|---:|
| Calories | 368.27 | 340 | 0 | 1880 | 240.27 |
| Calories from Fat | 127.10 | 100 | 0 | 1060 | 127.88 |
| Total Fat | 14.17 | 11 | 0 | 118 | 14.21 |
| Saturated Fat | 6.01 | 5 | 0 | 20 | 5.32 |
| Cholesterol | 54.94 | 35 | 0 | 575 | 87.27 |
| Sodium | 495.75 | 190 | 0 | 3600 | 577.03 |
| Carbohydrates | 47.35 | 44 | 0 | 141 | 28.25 |
| Dietary Fiber | 1.63 | 1 | 0 | 7 | 1.57 |
| Sugars | 29.42 | 17.5 | 0 | 128 | 28.68 |
| Protein | 13.34 | 12 | 0 | 87 | 11.43 |

---

### Categorical Features Summary

| Feature | Unique Values | Most Frequent Value | Frequency |
|---|---:|---|---:|
| Category | 9 | Coffee & Tea | 95 |
| Item | 260 | Egg McMuffin | 1 |
| Serving Size | 107 | 16 fl oz cup | 45 |

## Visualizations
### 1. Calories Distribution
![Calories Distribution](calories_distribution.png)

### 2. Average Calories by Category
![Average Calories by Category](avg_calories_by_category.png)

### 3. Correlation Matrix
![Correlation Matrix](correlation_matrix.png)

## Insights
- Calories are positively correlated with total fat and saturated fat.
- Some beverage categories have very low calories compared to meal-based categories.
- Sodium and cholesterol levels vary significantly across products.
- Nutritional values are highly skewed, indicating a few high-calorie menu items dominate the distribution.

## Conclusion
This EDA highlights nutritional trends across retail food menu items. The dataset can be further used for:
- Nutritional recommendation systems
- Menu optimization
- Customer health analytics
- Predictive modeling
