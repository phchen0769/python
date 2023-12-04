"""
Part 2. (sklearn is allowed)

Purpose: solving the problem of text analysis. In this task, we apply the method of support vector machine to determine which of the topics is news: atheism or space.
One of the reasons for the popularity of linear methods is that they work well on sparse data. So-called samples with a large number of features, where on each object most of the features are zero. Rare data occurs, for example, when working with texts. The fact is that the text is convenient to encode with a "bag of words" - formed as many features as all the unique words found in the texts, and the value of each feature is equal to the number of occurrences in the document of the word. It is clear that the total number of different languages ​​in a set of texts can reach tens of thousands, and only a small part of them will occur in one particular text.
It is possible to encode texts more cunningly, and to write not number of occurrences of a word in the text, and TF-IDF. This is an indicator that is equal to the product of two numbers: TF (term frequency) and IDF (inverse document frequency).
You will need to download the data first. In this task, we will use one of the datasets available in scikit-learn - 20 newsgroups. To do this, use the datasets module:

After executing this code, the text array will be in the newsgroups.data field, the class number - in the newsgroups.target field.
One of the difficulties with working with textual data is that they require a numerical representation. One way to find such a representation is to calculate the TF-IDF. In Scikit-Learn, this is implemented in the sklearn.feature_extraction.text.TfidfVectorizer class.
The conversion of the training sample should be done using the function fit_transform, test - using the transform.
The SVM classifier implementation is in the sklearn.svm.SVC class.
The weights of each attribute in the trained classifier are stored in the field coef_. It is convenient to select parameters using the sklearn.grid_search.GridSearchCV class (When using the scikit-learn library version 18.0.1 and higher sklearn.model_selection.GridSearchCV). Example of use:

When using the scikit-learn library version 18.0.1 and higher KFold is set a little differently:

The first argument in GridSearchCV is passed to the classifier for which values of parameters will be selected, the second - the dictionary (dict) defining a grid of parameters for search. Once the search is complete, you can analyze the quality values for all parameter values and choose the best option:

Instructions for execution:
1.Download objects from the newsset 20 newsgroups, which belong to the categories "space" and "atheism" (instructions above).
2.Calculate the TF-IDF characteristics for all texts. Note that in this task we offer you to calculate the TF-IDF for all data. In this approach, it turns out that the features on the training set use information from the test sample. This situation is perfectly legal, because we do not use the value of the target variable from the text. In practice, there are often situations when the characteristics of the objects of the test sample are known at the time of training, and therefore they can be used when learning the algorithm.
3.Select the minimum best parameter C from the set [10-5, 10-4, ... 104, 105] for SVM with a linear core (kernel = 'linear') using cross-validation of 5 blocks. Specify the random_state = 241 parameter for both SVM and KFold. As a precautionary quality, use the fate of the correct answers (accuracy).
4.Train the SVM throughout the sample with the best C parameter found in the previous step.
5.Find 10 words with the largest modulo weight. They are the answer to this task. Indicate them through a comma, in lowercase, in lexicographic order.

"""
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, KFold
import numpy as np

# 1. Download objects from the newsset 20 newsgroups
categories = ["alt.atheism", "sci.space"]
newsgroups = fetch_20newsgroups(
    subset="all", categories=categories, remove=("headers", "footers", "quotes")
)

# 2. Calculate the TF-IDF characteristics for all texts
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(newsgroups.data)
y = newsgroups.target

# 3. Select the minimum best parameter 'C'
param_grid = {"C": np.logspace(-5, 5, 11, base=10)}
kf = KFold(n_splits=5, shuffle=True, random_state=241)
grid = GridSearchCV(
    SVC(kernel="linear", random_state=241), param_grid, scoring="accuracy", cv=kf
)
grid.fit(X, y)

# Find the best parameter 'C'
best_C = grid.best_params_["C"]

# 4. Train the SVM throughout the sample with the best 'C' parameter
model = SVC(kernel="linear", C=best_C, random_state=241)
model.fit(X, y)

# 5. Find 10 words with the largest modulo weight
words = np.array(vectorizer.get_feature_names_out())
word_weights = model.coef_.toarray()[0]
sorted_word_indices = np.argsort(np.abs(word_weights))[-10:]
important_words = words[sorted_word_indices]
important_words_sorted = np.sort(important_words)

# Print the 10 most important words
print(",".join(important_words_sorted))
