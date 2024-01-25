import decrypt
import download
import file_system

# 输出文件名
video_name = input("Video name: ")

# m3u8读取
m3u8_file_name = "play.m3u8"
m3u8_content = file_system.m3u8_read(m3u8_file_name=m3u8_file_name)

# key读取
keys_file_name = "keys.txt"
keys = file_system.keys_read(keys_file_name=keys_file_name)

iv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 循环下载ts切片
file_index = 0

for line in m3u8_content:
    if not (".ts" in line):
        continue

    ts_url = line.split(".ts", 1)[0] + ".ts"  # 去除冗余信息

    # 下载ts切片
    print("Downloading ts file #{0}".format(file_index))
    download.ts_download(ts_url=ts_url)
    print("Downloaded ts file #{0}".format(file_index))

    # 解密
    print("Decrypting ts file #{0}".format(file_index))

    iv[14] = int(file_index / 256)
    iv[15] = int(file_index % 256)  # iv=16进制切片序号

    iv_b = bytes(i % 256 for i in iv)

    key_line = int(file_index / 20)  # key: 每20个切片为一组
    key_b = keys[key_line].encode("utf-8")

    decrypt.decrypt_data(key=key_b, iv=iv_b)
    print("Decrypted ts file #{0}".format(file_index))

    # 合并
    print("Merging ts file #{0}".format(file_index))
    file_system.merge_file(video_name=video_name)
    print("Merged ts file #{0}".format(file_index))

    file_index += 1
