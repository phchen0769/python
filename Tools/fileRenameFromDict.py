import os
import re

names_dict = {
    2506201: "安熙香",
    2506202: "曹心语",
    2506203: "陈政瀚",
    2506204: "仇万翔",
    2506205: "邓杰辉",
    2506206: "高朝威",
    2506207: "官思琦",
    2506208: "郭赋嵘",
    2506209: "郭健成",
    2506210: "韩泰瑜",
    2506211: "何颖乐",
    2506212: "胡静",
    2506213: "黄楷烯",
    2506214: "黄煜曦",
    2506216: "匡俊豪",
    2506217: "黎梓东",
    2506218: "李成国",
    2506219: "李东昱",
    2506220: "李嘉荣",
    2506221: "李世虎",
    2506222: "李维晋",
    2506223: "李元博",
    2506224: "李梓桦",
    2506225: "梁坚锋",
    2506226: "梁莹",
    2506227: "林嘉轩",
    2506228: "林炜锋",
    2506229: "刘嘉慧",
    2506230: "罗庚鸿",
    2506231: "罗宏为",
    2506232: "罗子淳",
    2506233: "罗梓峻",
    2506234: "马正锋",
    2506235: "莫浩燃",
    2506236: "潘俊霖",
    2506237: "邱恩琳",
    2506238: "邱泽兴",
    2506239: "邵子轩",
    2506240: "苏莉雯",
    2506241: "孙浩哲",
    2506242: "唐伟博",
    2506243: "徐家俊",
    2506244: "许凯威",
    2506245: "岩正华",
    2506246: "杨富涵",
    2506247: "杨梓霖",
    2506248: "姚纳铭",
    2506249: "姚志凯",
    2506250: "尹骏珲",
    2506251: "张斌斌",
    2506252: "钟竟轩",
    2506253: "周浩",
    2506254: "周宇航",
    2506255: "朱浩宇",
    2506256: "邹宇轩",
}


def rename_files(directory, names_dict):
    files = [
        f
        for f in os.listdir(directory)
        if re.search(r"\.(png|jpg|jpeg)$", f, re.IGNORECASE)
    ]
    files.sort()  # 可根据需要排序

    if len(files) != len(names_dict):
        print("文件数量与名单数量不一致，请检查！")
        return

    for i, (student_id, name) in enumerate(names_dict.items()):
        filename = files[i]
        ext = filename.split(".")[-1]
        new_filename = f"{name}{student_id}.{ext}"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)

        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"重命名: {filename} -> {new_filename}")
        else:
            print(f"文件已存在，跳过: {filename}")


if __name__ == "__main__":
    folder_path = "test02"  # 替换为实际路径
    rename_files(folder_path, names_dict)
