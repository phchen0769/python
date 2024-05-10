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

student_name_list = []
for i in student_grade:
    if i["姓名"] not in student_name_list:
        student_name_list.append(i["姓名"])

option = 6
while option != "q":
    print(
        """
        欢迎访问成绩管理系统
        1.查询所有学生成绩
        2.查询学生单科成绩以及总分
        3.计算全班平均成绩
        q.退出程序
        """
    )
    option = input("请输入你要执行的操作：")
    if option == "1":
        print(student_grade)
    elif option == "2":
        name = input("请输入需要查询的学生姓名：")
        if name not in student_name_list and student_grade.get("name"):
            print("没有找到该学生的信息。")

        else:
            name = input("请输入需要查询的学生姓名：")
            if name not in student_name_list and student_grade.get("name"):
                print("没有找到该学生的信息。")

            else:
                sum = 0
                for i in student_grade:
                    if student_grade["姓名"] == name:
                        sum = sum + i[""]
                print(sum)

    elif option == "3":
        chinese_sum = math_sum = english_sum = 0
        for i in student_grade:
            if i["科目"] == "语文":
                chinese_sum += i["成绩"]
            elif i["科目"] == "数学":
                math_sum += i["成绩"]
            else:
                english_sum += i["成绩"]
        print(
            f"语文平均成绩：{chinese_sum / len(student_name_list):.1f}",
        )
        print(f"数学平均成绩：{math_sum / len(student_name_list):.1f}")
        print(f"英语平均成绩：{english_sum / len(student_name_list):.1f}")
