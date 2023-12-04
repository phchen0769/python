import numpy as np
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.metrics import accuracy_score
import pandas as pd

# Assuming `data` is a Pandas DataFrame containing your dataset
data = pd.read_csv("./lab3/Iris.csv")

# Step 1: Select 2 column attributes
X = data[["PetalLengthCm", "PetalWidthCm"]].values
y = data["Species"].values

# Step 2: Select the value of k
k = 5

# Step 3: Divide the sample into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Step 4: KNN Classification
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2, axis=1))


def knn(X_train, y_train, X_test, k):
    y_pred = []

    for test_point in X_test:
        distances = euclidean_distance(X_train, test_point)
        k_indices = np.argsort(distances)[:k]  # Get the indices of k nearest neighbors
        k_nearest_labels = y_train[k_indices]  # Get the labels of k nearest neighbors

        # Majority vote, most common class label among the k-nearest neighbors
        most_common = Counter(k_nearest_labels).most_common(1)
        y_pred.append(most_common[0][0])

    return np.array(y_pred)


# Step 4.1 to 4.4: Predicting the class for the test set
y_pred = knn(X_train, y_train, X_test, k)

# Step 5: Calculate error
error = 1 - accuracy_score(y_test, y_pred)
print(f"Classification error: {error}")
