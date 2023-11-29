import pandas as pd


# 读取本地excle文件
def read_xlsx(file_name):
    data = pd.read_csv(file_name, index_col="PassengerId")
    return data


if __name__ == "__main__":
    data = read_xlsx("lab1/titanic.csv")
    count = 0
    for sex in data["Sex"]:
        if sex == "male":
            count += 1

    print(f"The number of man is {count}, the number of women is {len(data)-count}")
