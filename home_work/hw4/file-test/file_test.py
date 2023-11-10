try:
    file_path = "file-test.txt"
    result = False

    with open(file_path, mode="r") as f:
        for line in f:
            if "\n" in line:
                line = line[0:-1]

            arr = line.split(";")
            temp_arr = arr[0].split()
            temp_arr = list(map(int, temp_arr))
            whole_part = sum(temp_arr) // len(temp_arr)
            remainder = sum(temp_arr) % len(temp_arr)
            excepted_temp_arr = arr[1].split()
            excepted_temp_arr = list(map(int, excepted_temp_arr))
            excepted_whole_part, excepted_remainder = excepted_temp_arr

            if whole_part == excepted_whole_part and remainder == excepted_remainder:
                result = True
            else:
                result = False

            print(f"{line} {result}")
except Exception as e:
    print(e)
