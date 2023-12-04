import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import Ridge
from scipy.sparse import hstack

# Assuming the dataset has been saved in the 'salary-train.csv' file
# 1. Load the dataset
df = pd.read_csv("./lab4/salary-train.csv")

# 2. Data preprocessing

# a. Convert FullDescription to lowercase
df["FullDescription"] = df["FullDescription"].str.lower()

# b. Replace all non-alphanumeric characters with spaces
df["FullDescription"] = df["FullDescription"].replace("[^a-zA-Z0-9]", " ", regex=True)

# c. Use TfidfVectorizer to transform text into TF-IDF feature vectors
tfidf = TfidfVectorizer(min_df=5)
X_text = tfidf.fit_transform(df["FullDescription"])

# d. Replace missing values in LocationNormalized and ContractTime with 'nan'
df["LocationNormalized"].fillna("nan", inplace=True)
df["ContractTime"].fillna("nan", inplace=True)

# e. Use DictVectorizer for one-hot encoding of LocationNormalized and ContractTime
enc = DictVectorizer()
X_categorical = enc.fit_transform(
    df[["LocationNormalized", "ContractTime"]].to_dict("records")
)

# f. Combine the feature matrices
X = hstack([X_text, X_categorical])

# The target variable
y = df["SalaryNormalized"]

# 3. Train the ridge regression model
ridge_regressor = Ridge(alpha=1.0)
ridge_regressor.fit(X, y)
