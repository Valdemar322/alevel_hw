try:
    user_value = int(input("Enter odd positive number: "))
    if user_value > 0:
        star = "*"
        space = " " * (user_value // 2)
        result = ""
        for y in range(user_value):
            if y > user_value // 2:
                space += " "
                star = star[0:-2]
            else:
                if y > 0:
                    space = space[0:-1]
                    star += "*" * 2
            result = space + star
            print(result)
    else:
        print(f"You are entered negative number! or 0!")

except Exception as e:
    print(e)
