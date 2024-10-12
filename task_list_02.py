"""
给定一个字符串列表 words = ["apple", "banana", "cherry", "date"]，完成以下任务：

将所有单词转换为小写。
找出并返回列表中最长的单词。
添加一个新单词 "elderberry" 到列表末尾。
删除以 'a' 开头的单词，并输出新列表。
"""
words = ["apple", "banana", "cherry", "date"]

# 1. 将所有单词转换为小写
lowercase_words = [word.lower() for word in words]
print("Lowercase Words:", lowercase_words)

# 2. 找出并返回列表中最长的单词
longest_word = max(words, key=len)
print("Longest Word:", longest_word)

# 3. 添加一个新单词 "elderberry" 到列表末尾
words.append("elderberry")
print("Updated List:", words)

# 4. 删除以 'a' 开头的单词，并输出新列表
filtered_words = [word for word in words if not word.startswith('a')]
print("Filtered Words:", filtered_words)
