"""
给定一个嵌套列表 nested_list = [[1, 2], [3, 4], [5, 6]]，完成以下任务：

将每个子列表的第一个元素加1。
扁平化嵌套列表，生成一个新的一维列表。
移除列表中的重复元素。
对列表进行排序。

"""
nested_list = [[1, 2], [3, 4], [5, 6]]

# 1. 将每个子列表的第一个元素加1
updated_nested_list = [[sub[0] + 1, sub[1]] for sub in nested_list]
print("Updated Nested List:", updated_nested_list)

# 2. 扁平化嵌套列表，生成一个新的一维列表
flat_list = [item for sublist in updated_nested_list for item in sublist]
print("Flat List:", flat_list)

# 3. 移除列表中的重复元素
unique_list = list(set(flat_list))
print("Unique List:", unique_list)

# 4. 对列表进行排序
sorted_list = sorted(unique_list)
print("Sorted List:", sorted_list)
