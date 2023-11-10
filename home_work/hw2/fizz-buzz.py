try:
    fizz = int(input("Enter first number: "))
    buzz = int(input("Enter second number: "))
    user_number_range = int(input("Enter third number: "))

    for num in range(1, user_number_range + 1):
        if not num % buzz and not num % fizz:
            num = "FB"
        elif not num % buzz:
            num = "B"
        elif not num % fizz:
            num = "F"
        print(f"{num} ", end="")
except Exception as e:
    print(e)
