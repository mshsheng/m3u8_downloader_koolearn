import os


# 创建新文件夹
def create_directory(directory_name):
    os.system("mkdir {0}".format(directory_name))


# 读取m3u8文件
def m3u8_read(m3u8_file_name):
    with open(m3u8_file_name, "r") as file_read:
        m3u8_content = file_read.readlines()
        file_read.close()
    m3u8_content = [line.strip("\n") for line in m3u8_content]
    return m3u8_content


# 读取key文件
def keys_read(keys_file_name):
    with open(keys_file_name, "r") as file_read:
        keys = file_read.readlines()
        file_read.close()
    keys = [line.strip("\n") for line in keys]
    return keys


# 写文件
def write_file(path, data):
    with open(path, "wb") as file_write:  # wb:覆盖式二进制写入
        file_write.write(data)
        file_write.close()


# 合并文件
def merge_file(video_name):
    file_read = open("temp_d.ts", "rb")
    data = file_read.read()

    with open(video_name + ".ts", "ab") as file_write:  # ab:追加式二进制写入
        file_write.write(data)
        file_write.close()

    file_read.close()
