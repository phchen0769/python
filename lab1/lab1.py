import pandas as pd

# Load the Titanic dataset
data = pd.read_csv("./lab1/titanic.csv")

# 1. Count the number of men and women
gender_counts = data["Sex"].value_counts()
men_count = gender_counts["male"]
women_count = gender_counts["female"]
print(f"Number of men and women on the ship: {men_count} {women_count}")

# 2. Calculate the percentage of surviving passengers
survived_count = data["Survived"].sum()
total_passengers = len(data)
survival_percentage = (survived_count / total_passengers) * 100
print(f"Percentage of passengers who survived: {survival_percentage:.2f}")

# 3. Calculate the percentage of first class passengers
first_class_count = data["Pclass"].value_counts()[1]
first_class_percentage = (first_class_count / total_passengers) * 100
print(f"Percentage of first class passengers: {first_class_percentage:.2f}")

# 4. Calculate the average and median age of the passengers
average_age = data["Age"].mean()
median_age = data["Age"].median()
print(f"Average age of passengers: {average_age:.2f}")
print(f"Median age of passengers: {median_age:.2f}")

# 5. Calculate the Pearson correlation between SibSp and Parch
correlation = data["SibSp"].corr(data["Parch"])
print(f"Pearson correlation between SibSp and Parch: {correlation:.2f}")

# 6. Extract the most popular female name
female_names = data[data["Sex"] == "female"]["Name"]
first_names = female_names.apply(lambda x: x.split(",")[1].split()[0])
most_popular_name = first_names.value_counts().index[0]
print(f"The most popular female name on the ship: {most_popular_name}")
