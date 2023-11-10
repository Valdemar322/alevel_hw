try:
    user_number = int(input("Enter a number:"))
    if user_number > 0:
        print(f"Divisors of {user_number}: ", end="")
        for num in range(1, user_number + 1):
            if not user_number % num:
                print(f"{num} ", end="")
    else:
        print("The value must be greater than zero")
except Exception as e:
    print(e)
