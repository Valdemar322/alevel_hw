import random

random_values = ""
write_line = ""

# write random values in string(random_values)
for line in range(20):
    for value in range(3):
        val = random.randint(1, 20)
        random_values += str(val) + " "
    random_values += "\n"

# write string with random values in file
with open("random_fizzbuzz.txt", mode="w") as f:
    f.write(random_values)

with open("random_fizzbuzz.txt", mode="r") as f:
    for line in f:
        line_values = line.split(' ')
        int_line_values = []

        for x in line_values:
            if x == "\n":
                pass
            else:
                int_line_values.append(x)

        line_values = list(map(int, int_line_values))

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
