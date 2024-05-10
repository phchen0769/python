"以下程序的运行结果是______"
person = {
    "身份证号": "110112XXXXXXXX0101",
    "姓名": "王宏",
    "性别": "男",
    "居住地": "北京市XX区xX街道XX小区",
}
person["居住地"] = "北京市通州区"
person["电话"] = 13801010101
print(person)


# # 直接创建
# person1 = {
#     "身份证号": "110112XXXXXXXX0101",
#     "姓名": "王宏",
#     "性别": "男",
#     "居住地": "北京市XX区XX街道XX小区",
# }

# # 通过其他字典创建
# person2 = dict(person1)

# # 通过键值对的序列创建
# person3 = dict(
#     [
#         ("身份证号", "110112XXXXXXXX0101"),
#         ("姓名", "王宏"),
#         ("性别", "男"),
#         ("居住地", "北京市XX区XX街道XX小区"),
#     ]
# )

# person4 = dict(
#     身份证号="110112XXXXXXXX0101",
#     姓名="王宏",
#     性别="男",
#     居住地="北京市XX区XX街道XX小区",
# )
# # 通过关键字参数创建
# person5 = dict(
#     zip(
#         ["身份证号", "姓名", "性别", "居住地"],
#         ["110112XXXXXXXX0101", "王宏", "男", "北京市XX区XX街道XX小区"],
#     )
# )
# # 通过 dict 和zip结合创建
# print(person1["姓名"])
# print(person2.get("姓名"))
# print(person1)
# print(person2)
# print(person3)
# print(person4)
# print(person5)
