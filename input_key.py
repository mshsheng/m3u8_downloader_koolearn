print(
    "Please input key strings here to make the key file.\nIf there is no more keys, input 'q' to quit.\n"
)

loop_num = 0

while True:
    key = input(
        "Please input the key for ts#{0} to ts#{1}: ".format(
            str(loop_num * 20), str((loop_num + 1) * 20 - 1)
        )
    )

    if key == "q":
        break

    key += "\n"
    with open("keys.txt", "a") as file_write:
        file_write.write(key)
        file_write.close()

    loop_num += 1
