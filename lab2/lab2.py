import pandas as pd
import numpy as np
import seaborn as sns

# Load the dataset
dataset = pd.read_csv(
    "./lab2/Energy_and_Water_Data_Disclosure_for_Local_Law_84_2017__Data_for_Calendar_Year_2016_.csv"
)

# Convert "Not Available" entries to NaN
dataset.replace("Not Available", np.nan, inplace=True)

# Convert number types to float and "Not Available" to NaN
dataset = dataset.apply(pd.to_numeric, errors="coerce")

# Remove rows with missing or invalid values
dataset = dataset.dropna()


# Estimate missing data
missing_data_percentage = dataset.isnull().sum() / len(dataset) * 100

# Remove features with more than 50% missing data
dataset = dataset.loc[:, missing_data_percentage < 50]

# Remove outliers using box plot fences
Q1 = dataset.quantile(0.25)
Q3 = dataset.quantile(0.75)
IQ = Q3 - Q1
lower_fence = Q1 - 3 * IQ
upper_fence = Q3 + 3 * IQ
dataset = dataset[~((dataset < lower_fence) | (dataset > upper_fence)).any(axis=1)]

# Exploratory Data Analysis
# Density plot between Energy Star Scores and Primary Property Type
sns.kdeplot(
    data=dataset, x="Energy Star Scores", hue="Primary Property Type - Self Selected"
)

# Density plot between Energy Star Scores and Borough
sns.kdeplot(data=dataset, x="Energy Star Scores", hue="Borough")

# Calculate correlations
correlations = dataset.corr()

# Find the feature showing the better difference between types
feature_type_diff = (
    correlations["Energy Star Scores"]
    .abs()
    .groupby(dataset["Primary Property Type - Self Selected"])
    .mean()
)
best_feature_type_diff = feature_type_diff.idxmax()

# Find the biggest and lowest correlation with Energy Star Scores
correlation_with_energy_star_scores = correlations["Energy Star Scores"].drop(
    "Energy Star Scores"
)
biggest_correlation = correlation_with_energy_star_scores.idxmax()
lowest_correlation = correlation_with_energy_star_scores.idxmin()

# Feature Engineering and Selection
# One-hot encoding of categorical features
categorical_features = ["Borough", "Primary Property Type - Self Selected"]
dataset = pd.get_dummies(dataset, columns=categorical_features)

# Taking the logarithm of numerical data
numerical_data = dataset.select_dtypes(include=[np.number])
dataset[numerical_data.columns] = np.log(dataset[numerical_data.columns])

# Selection - removing collinear features
collinear_features = set()
for i in range(len(correlation_with_energy_star_scores)):
    for j in range(i):
        if abs(correlation_with_energy_star_scores.iloc[i, j]) > 0.6:
            colname_i = correlation_with_energy_star_scores.columns[i]
            colname_j = correlation_with_energy_star_scores.columns[j]
            collinear_features.add(
                colname_i
                if feature_type_diff[colname_i] < feature_type_diff[colname_j]
                else colname_j
            )
dataset.drop(collinear_features, axis=1, inplace=True)
