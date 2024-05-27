# 任务1：存储成绩
table = [
    {"序号": 1, "姓名": "王静文", "语文": 90, "数学": 85, "英语": 76},
    {"序号": 2, "姓名": "康力", "语文": 50, "数学": 99, "英语": 78},
    {"序号": 3, "姓名": "刘聪", "语文": 86, "数学": 74, "英语": 90},
]


# 任务2-1：计算学生总分
# 遍历table数据
for student in table:
    score = student["语文"] + student["数学"] + student["英语"]
    # 打印每个学生的姓名和总分
    print(f"{student['姓名']}的总分是：{score}")


# 任务2-2：计算语数英平均分
# 初始化语数英班级总分为0分
chinese = math = english = 0
# 遍历table数据
for student in table:
    chinese = student["语文"]
    math = student["数学"]
    english = student["英语"]

print(
    f"语文平均成绩：{chinese / len(table):.1f}",
)
print(f"数学平均成绩：{math / len(table):.1f}")
print(f"英语平均成绩：{english / len(table):.1f}")
