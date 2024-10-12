"""
给定一个整数列表 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，完成以下任务：

提取列表中的前三个元素。
提取列表中从索引2到索引7的元素（不包括索引7）。
提取列表中的偶数元素。
提取列表中每隔两个元素的值。
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. 提取列表中的前三个元素
first_three = numbers[:3]
print("First Three:", first_three)

# 2. 提取列表中从索引2到索引7的元素（不包括索引7）
sliced_list = numbers[2:7]
print("Sliced List:", sliced_list)

# 3. 提取列表中的偶数元素
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even Numbers:", even_numbers)

# 4. 提取列表中每隔两个元素的值
every_second = numbers[::2]
print("Every Second:", every_second)
