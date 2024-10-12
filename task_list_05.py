"""
给定一个字符串列表 words = ["apple", "banana", "cherry", "date"]，完成以下任务：

创建一个新列表，其中包含长度大于等于5的单词。
创建一个新列表，其中包含以 'a' 开头且长度小于等于4的单词。
创建一个新列表，其中包含原列表中每个单词的长度。
"""

words = ["apple", "banana", "cherry", "date"]

# 1. 创建一个新列表，其中包含长度大于等于5的单词
long_words = [word for word in words if len(word) >= 5]
print("Long Words:", long_words)

# 2. 创建一个新列表，其中包含以 'a' 开头且长度小于等于4的单词
short_a_words = [word for word in words if word.startswith('a') and len(word) <= 4]
print("Short A-Words:", short_a_words)

# 3. 创建一个新列表，其中包含原列表中每个单词的长度
lengths = [len(word) for word in words]
print("Lengths:", lengths)
