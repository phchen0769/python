import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv(
    "./lab2/Energy_and_Water_Data_Disclosure_for_Local_Law_84_2017__Data_for_Calendar_Year_2016_.csv"
)

# 1. Data cleansing
# Replace "Not Available" with NaN and attempt to convert columns to float.
for col in df.columns:
    # Attempt to replace 'Not Available' and convert to float if possible.
    df[col] = pd.to_numeric(df[col].replace("Not Available", np.nan), errors="coerce")

# 2. Find Missing Data and Outliers
# a. Remove columns with more than 50% missing data
half_count = len(df) / 2
df = df.dropna(thresh=half_count, axis=1)

# b. Remove outliers based on the interquartile range (IQR)
for col in df.select_dtypes(include=["float64", "int64"]).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_fence = Q1 - 3 * IQR
    upper_fence = Q3 + 3 * IQR
    df = df[(df[col] >= lower_fence) & (df[col] <= upper_fence)]


# 3. Conduct Exploratory Data Analysis
# a. Density plot between Energy Star Scores and other features
def plot_density(feature):
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df, x="ENERGY STAR Score", hue=feature, common_norm=False)
    plt.title(f"Density Plot of ENERGY STAR Score and {feature}")
    plt.xlabel("ENERGY STAR Score")
    plt.ylabel("Density")
    plt.show()


plot_density("Primary Property Type - Self Selected")
plot_density("Borough")

# b. Find the biggest and the lowest correlation with 'ENERGY STAR Score'
correlations = df.corr()["ENERGY STAR Score"].sort_values()

print("Most Positive Correlations with ENERGY STAR Score:\n", correlations.tail(5))
print("\nMost Negative Correlations with ENERGY STAR Score:\n", correlations.head(5))

# 4. Feature Engineering and Selection
# a. One-hot coding of categorical features
df = pd.get_dummies(df, columns=["Borough", "Primary Property Type - Self Selected"])

# b. Taking the logarithm of numerical data
for col in df.select_dtypes(include=["float64", "int64"]).columns:
    df[col] = df[col].apply(lambda x: np.log1p(x) if x > 0 else x)

# c. Removal of collinear features
collinear_features = set()
for i in range(len(correlations)):
    for j in range(i):
        if abs(correlations.iloc[i, j]) > 0.6:
            colname = correlations.columns[i]
            collinear_features.add(colname)

df = df.drop(columns=collinear_features)

# The dataframe df is now ready for modeling
