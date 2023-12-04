"""
Part 1. (mandatory without sklearn)
Purpose: In this laboratory work it is necessary to classify Fisher's irises by the support vector machine method. Data on iris flowers are used for classification. The target column corresponds to the type of flower (‘Species’).
The Support Vector Machine (SVM) method is one of the types of linear classifiers. The functionality it optimizes is aimed at maximizing the width of the dividing strips between classes. From the theory of statistical training it is known that this width is closely connected with the generalization ability of the algorithm, and its maximization allows it to avoid the overfitting.
The method of support vector machines has another feature. If we transform its optimization problem, it turns out that the final classifier can be represented as a weighted sum of the scalar products of this object to the objects of the training sample.
In essence, the algorithm makes predictions based on the similarity of the new object with the objects of the training sample. In this case, as a rule, not all coefficients are non-zero. This means that the classification is based on similarities with only part of the training facilities. Such objects are called reference.
Task:
1.Leave only two classes in the target column (Delete Setosa data). At this stage, we assume that the classes are linearly separated
2.Select 2 columns for classification: length (‘PetalLengthCm’) and width (‘PetalWidthCm’) of the flower.
3.Divide the sample into training (80%) and test (20%) randomly, because the data is organized.
4.Find the hyperplane that separates the two classes. (in our case it is a line)
5.Next, you need to maximize the length to the hyperline (2m) from the nearest objects in each class. Note that the line is determined by the distance of the nearest data point to the hyperplane. Which means that the classifier depends only on a small set of learning data, called support vectors. The example is shown in Figure 1.

Figure 1. Selection of reference points

To check the correct operation of the algorithm, calculate the error. Evaluate the result of your classification with the original data.
"""
import pandas as pd
import numpy as np

# Assuming iris data is loaded into DataFrame `df`
df = pd.read_csv("./lab5/Iris.csv")

# 1. Remove Setosa species from the dataset
df = df[df["Species"] != "Iris-setosa"]

# Convert species into numerical values
species_to_num = {"Iris-versicolor": -1, "Iris-virginica": 1}
df["Species"] = df["Species"].map(species_to_num)

# 2. Select the 'PetalLengthCm' and 'PetalWidthCm' columns for classification
X = df[["PetalLengthCm", "PetalWidthCm"]].values
y = df["Species"].values

# 3. Split the data into training (80%) and test (20%) sets
np.random.seed(42)  # Set seed for reproducibility
perm = np.random.permutation(len(X))
split_index = int(len(X) * 0.8)
X_train, X_test = X[perm[:split_index]], X[perm[split_index:]]
y_train, y_test = y[perm[:split_index]], y[perm[split_index:]]


# 4. Implement a simple SVM algorithm
# Note: This is a very simplified version and does not include kernels or optimization techniques typically found in SVM.
def svm_fit(X, y, epochs=1000, eta=0.01):
    w = np.zeros(X.shape[1])
    b = 0
    for _ in range(epochs):
        for xi, yi in zip(X, y):
            if yi * (np.dot(xi, w) - b) >= 1:
                w -= eta * (2 * 1 / epochs * w)
            else:
                w -= eta * (2 * 1 / epochs * w - np.dot(xi, yi))
                b -= eta * yi
    return w, b


w, b = svm_fit(X_train, y_train)


# 5. Prediction function
def svm_predict(X, w, b):
    return np.sign(np.dot(X, w) - b)


# Check the algorithm's accuracy
def svm_accuracy(X, y, w, b):
    predictions = svm_predict(X, w, b)
    return np.mean(predictions == y)


train_accuracy = svm_accuracy(X_train, y_train, w, b)
test_accuracy = svm_accuracy(X_test, y_test, w, b)

print(f"Training Accuracy: {train_accuracy}")
print(f"Testing Accuracy: {test_accuracy}")
