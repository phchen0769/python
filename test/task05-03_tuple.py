"""
   创建一个元组 fruits = ('apple', 'banana', 'cherry')，将其中的水果名称转换为大写形式并存储在一个新的元组中。
"""

fruits = ("apple", "banana", "cherry")
uppercased_fruits = tuple(fruit.upper() for fruit in fruits)
print(uppercased_fruits)
