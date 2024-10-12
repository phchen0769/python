"""
给定一个整数列表 numbers = [1, 2, 3, 4, 5]，完成以下任务：

计算列表中所有数字的和。
找到并返回列表中的最大值和最小值。
将列表中的所有数字乘以2,并输出新列表。
删除列表中的偶数，并输出新列表。
"""
numbers = [1, 2, 3, 4, 5]

# 1. 计算列表中所有数字的和
total_sum = sum(numbers)
print("Sum:", total_sum)

# 2. 找到并返回列表中的最大值和最小值
max_value = max(numbers)
min_value = min(numbers)
print("Max:", max_value, "Min:", min_value)

# 3. 将列表中的所有数字乘以2，并输出新列表
doubled_numbers = [num * 2 for num in numbers]
print("Doubled List:", doubled_numbers)

# 4. 删除列表中的偶数，并输出新列表
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd Numbers:", odd_numbers)
