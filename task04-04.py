"""
使用列表从键盘接收五个输入,分别是浮点数，运算符(+-*/)，浮点数，运算符(+-*/),浮点数
输出计算后的答案。
1
+
2
*
3
"""

list1 = []
operator = []
result = 0
# list1.append(input("请输入一个浮点数:"))
# list1.append(input("请输入一个操作符:"))
# list1.append(input("请输入一个浮点数:"))
# list1.append(input("请输入一个操作符:"))
# list1.append(input("请输入一个浮点数:"))
list1 = [1, "-", 3, "/", 2]
# 判断符号优先级
if list1[3] == "*" or list1[3] == "/":
    if list1[1] == "+" or list1[1] == "-":
        operator.append(1)
        operator.append(3)
    else:
        operator.append(3)
        operator.append(1)
else:
    operator.append(3)
    operator.append(1)

if list1[operator[-1]] == "+":
    result = float(list1[operator[-1] - 1]) + float(list1[operator[-1] + 1])
elif list1[operator[-1]] == "-":
    result = float(list1[operator[-1] - 1]) - float(list1[operator[-1] + 1])
elif list1[operator[-1]] == "*":
    result = float(list1[operator[-1] - 1]) * float(list1[operator[-1] + 1])
elif list1[operator[-1]] == "/":
    result = float(list1[operator[-1] - 1]) / float(list1[operator[-1] + 1])

# 去除已经运算过的操作符
operator.pop()

if operator[-1] == 1:
    if list1[operator[-1]] == "+":
        result = float(list1[operator[-1] - 1]) + result
    elif list1[operator[-1]] == "-":
        result = float(list1[operator[-1] - 1]) - result
    elif list1[operator[-1]] == "*":
        result = float(list1[operator[-1] - 1]) * result
    elif list1[operator[-1]] == "/":
        result = float(list1[operator[-1] - 1]) / result
else:
    if list1[operator[-1]] == "+":
        result = float(list1[operator[-1] + 1]) + result
    elif list1[operator[-1]] == "-":
        result = float(list1[operator[-1] + 1]) - result
    elif list1[operator[-1]] == "*":
        result = float(list1[operator[-1] + 1]) * result
    elif list1[operator[-1]] == "/":
        result = float(list1[operator[-1] + 1]) / result

print(result)
