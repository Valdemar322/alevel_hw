try:
    count = True
    user_number = int(input("Enter a number:"))
    if user_number >= 0:
        print(f"Rank and multipliers of {user_number}: ", end="")
        for num in reversed(range(len(str(user_number)))):
            if not num:
                count = not count
            rank = 10 ** num
            mul = user_number // rank
            user_number %= rank
            print(f" {mul} * {rank}(10^{num}) {'+' * count}", end="")
    else:
        print("The value must be equal or greater than zero")
except Exception as e:
    print(e)
