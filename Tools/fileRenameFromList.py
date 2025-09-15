import os
import re

names = [
    "安熙香",
    "曹心语",
    "陈政瀚",
    "仇万翔",
    "邓杰辉",
    "高朝威",
    "官思琦",
    "郭赋嵘",
    "郭健成",
    "韩泰瑜",
    "何颖乐",
    "胡静",
    "黄楷烯",
    "黄煜曦",
    "匡俊豪",
    "黎梓东",
    "李成国",
    "李东昱",
    "李嘉荣",
    "李世虎",
    "李维晋",
    "李元博",
    "李梓桦",
    "梁坚锋",
    "梁莹",
    "林嘉轩",
    "林炜锋",
    "刘嘉慧",
    "罗庚鸿",
    "罗宏为",
    "罗子淳",
    "罗梓峻",
    "马正锋",
    "莫浩燃",
    "潘俊霖",
    "邱恩琳",
    "邱泽兴",
    "邵子轩",
    "苏莉雯",
    "孙浩哲",
    "唐伟博",
    "徐家俊",
    "许凯威",
    "岩正华",
    "杨富涵",
    "杨梓霖",
    "姚纳铭",
    "姚志凯",
    "尹骏珲",
    "张斌斌",
    "钟竟轩",
    "周浩",
    "周宇航",
    "朱浩宇",
    "邹宇轩",
]


def rename_files(directory, names):
    files = [
        f
        for f in os.listdir(directory)
        if re.search(r"\.(png|jpg|jpeg)$", f, re.IGNORECASE)
    ]
    files.sort()  # 可根据需要排序

    if len(files) != len(names):
        print("文件数量与名单数量不一致，请检查！")
        return

    for i, filename in enumerate(files):
        ext = filename.split(".")[-1]
        new_filename = f"{names[i]}.{ext}"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)

        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"重命名: {filename} -> {new_filename}")
        else:
            print(f"文件已存在，跳过: {filename}")


if __name__ == "__main__":
    folder_path = "test02"  # 替换为实际路径
    rename_files(folder_path, names)
