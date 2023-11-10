try:
    write_line = ""
    with open("fizzbuzz.txt", mode="r") as f:
        for line in f:
            line_values = line.split(' ')
            line_values = list(map(int, line_values))

            for num in range(1, line_values[-1] + 1):
                if not num % line_values[1] and not num % line_values[0]:
                    num = "FB"
                    write_line += "FB "
                elif not num % line_values[1]:
                    num = "B"
                    write_line += "B "
                elif not num % line_values[0]:
                    num = "F"
                    write_line += "F "
                else:
                    write_line += str(num) + " "
                print(f"{num} ", end="")
            print()
            write_line += "\n"

    with open("fizzbuzz_result.txt", mode="w") as file:
        file.write(write_line)

except Exception as e:
    print(e)
