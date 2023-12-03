import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from math import log2

# Load the Iris dataset
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["Species"] = iris.target

# Rename columns for easier access
df.columns = [
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm",
    "Species",
]

# Select the columns for classification
df = df[["PetalLengthCm", "PetalWidthCm", "Species"]]

# Split the data into train and test sets
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)


# Function to calculate entropy of the given data set
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy = sum(
        (-counts[i] / np.sum(counts)) * log2(counts[i] / np.sum(counts))
        for i in range(len(elements))
    )
    return entropy


# Function to calculate information gain
def info_gain(data, split_attribute_name, target_name="Species"):
    total_entropy = entropy(data[target_name])
    vals, counts = np.unique(data[split_attribute_name], return_counts=True)
    weighted_entropy = sum(
        (counts[i] / np.sum(counts))
        * entropy(
            data.where(data[split_attribute_name] == vals[i]).dropna()[target_name]
        )
        for i in range(len(vals))
    )
    information_gain = total_entropy - weighted_entropy
    return information_gain


# The ID3 algorithm
def ID3(
    data,
    originaldata,
    features,
    target_attribute_name="Species",
    parent_node_class=None,
):
    # If all target_values have the same value, return this value
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]

    # If the dataset is empty, return the mode target feature value in the original dataset
    elif len(data) == 0:
        return np.unique(originaldata[target_attribute_name])[
            np.argmax(
                np.unique(originaldata[target_attribute_name], return_counts=True)[1]
            )
        ]

    # If the feature space is empty, return the mode target feature value of the direct parent node
    elif len(features) == 0:
        return parent_node_class

    # If none of the above conditions holds true, grow the tree!
    else:
        # Set the default value for this node --> The mode target feature value of the current node
        parent_node_class = np.unique(data[target_attribute_name])[
            np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])
        ]

        # Select the feature which best splits the dataset
        item_values = [
            info_gain(data, feature, target_attribute_name) for feature in features
        ]  # Return the information gain values for the features in the dataset
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]

        # Create the tree structure. The root gets the name of the feature (best_feature) with the maximum information gain in the first run
        tree = {best_feature: {}}

        # Remove the feature with the best info gain from the feature space
        features = [i for i in features if i != best_feature]

        # Grow a branch under the root node for each possible value of the root node feature

        for value in np.unique(data[best_feature]):
            value = value
            # Split the dataset along the value of the feature with the largest information gain and create sub_datasets
            sub_data = data.where(data[best_feature] == value).dropna()

            # Call the ID3 algorithm for each of those sub_datasets with the new parameters --> Here the recursion comes in!
            subtree = ID3(
                sub_data, df, features, target_attribute_name, parent_node_class
            )

            # Add the sub tree, grown from the sub_dataset to the tree under the root node
            tree[best_feature][value] = subtree

        return tree


# Construct the tree using the ID3 algorithm
tree = ID3(train_data, train_data, train_data.columns[:-1])

print(tree)
