from Crypto.Cipher import AES


# 解密文件
def decrypt_data(key, iv):
    with open("temp_e.ts", "rb") as file_read:
        src = file_read.read()
        file_read.close()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    output_bytes = cipher.decrypt(src)

    with open("temp_d.ts", "wb") as file_write: # "d" stands for "decrypted"
        file_write.write(output_bytes)
        file_write.close()
