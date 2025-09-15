import os
import re


def rename_files(directory):
    # 只保留第一个下划线前的姓名和扩展名
    pattern = re.compile(r"^([^_]+).*?\.(png|jpg|jpeg)$", re.IGNORECASE)

    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            name = match.group(1)  # 提取姓名
            ext = match.group(2)  # 提取扩展名
            new_filename = f"{name}.{ext}"

            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            # 避免覆盖同名文件
            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
                print(f"重命名: {filename} -> {new_filename}")
            else:
                print(f"文件已存在，跳过: {filename}")


if __name__ == "__main__":
    folder_path = "test02"  # 替换为实际路径
    rename_files(folder_path)
