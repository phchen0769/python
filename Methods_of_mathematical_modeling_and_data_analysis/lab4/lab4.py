import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import Ridge
from scipy.sparse import hstack
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the data
df = pd.read_csv("salary-train.csv")

# Preprocessing
# Convert texts to lowercase and replace non-letter and non-number characters with spaces
df["FullDescription"] = (
    df["FullDescription"].str.lower().replace("[^a-zA-Z0-9]", " ", regex=True)
)

# Replace NaN values in 'LocationNormalized' and 'ContractTime' with 'nan'
df["LocationNormalized"].fillna("nan", inplace=True)
df["ContractTime"].fillna("nan", inplace=True)

# Convert text features to TF-IDF features
vectorizer = TfidfVectorizer(min_df=5)
X_tfidf = vectorizer.fit_transform(df["FullDescription"])

# One-hot encode categorical features
encoder = DictVectorizer()
X_categorical = encoder.fit_transform(
    df[["LocationNormalized", "ContractTime"]].to_dict("records")
)

# Combine all features into one feature matrix
X_combined = hstack([X_tfidf, X_categorical])

# Target variable
y = df["SalaryNormalized"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_combined, y, test_size=0.2, random_state=42
)

# Initialize and train the Ridge regression model
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

# Predict and evaluate the model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")
