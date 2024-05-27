# 任务1：存储学生数据
student_grade = [
    {"序号": 1, "姓名": "王静文", "科目": "语文", "成绩": 90},
    {"序号": 2, "姓名": "王静文", "科目": "数学", "成绩": 85},
    {"序号": 3, "姓名": "王静文", "科目": "英语", "成绩": 76},
    {"序号": 4, "姓名": "康力", "科目": "语文", "成绩": 50},
    {"序号": 5, "姓名": "康力", "科目": "数学", "成绩": 99},
    {"序号": 6, "姓名": "康力", "科目": "英语", "成绩": 78},
    {"序号": 7, "姓名": "刘聪", "科目": "语文", "成绩": 86},
    {"序号": 8, "姓名": "刘聪", "科目": "数学", "成绩": 74},
    {"序号": 9, "姓名": "刘聪", "科目": "英语", "成绩": 90},
]

# 任务2：取出学生姓名
student_name_list = []
for i in student_grade:
    if i["姓名"] not in student_name_list:
        student_name_list.append(i["姓名"])

# 遍历学生姓名列表
for name in student_name_list:
    sum = 0
    # 遍历学生成绩列表
    for student in student_grade:
        if student["姓名"] == name:
            sum = sum + student["成绩"]
    print(name + " : " + str(sum))


# 初始化语数英班级总分为0分
chinese_sum = math_sum = english_sum = 0
for i in student_grade:
    if i["科目"] == "语文":
        chinese_sum += i["成绩"]
    elif i["科目"] == "数学":
        math_sum += i["成绩"]
    else:
        english_sum += i["成绩"]
print(
    f"语文平均成绩：{chinese_sum / len(student_name_list)}",
)
print(f"数学平均成绩：{math_sum / len(student_name_list)}")
print(f"英语平均成绩：{english_sum / len(student_name_list)}")
