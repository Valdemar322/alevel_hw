banknotes = [10, 20, 50, 100, 200, 500, 1000]

count_10 = 0
count_20 = 0
count_50 = 0
count_100 = 0
count_200 = 0
count_500 = 0
count_1000 = 0

amount_of_money = int(input("Enter amount of money what do you want to recieve: "))

while amount_of_money:

    if amount_of_money >= 1000:
        if not amount_of_money % banknotes[-1]:
            count_1000 = amount_of_money // 1000
            amount_of_money = 0
        else:
            remainder = amount_of_money % 1000
            count_1000 = amount_of_money // 1000
            amount_of_money = remainder

    elif 500 <= amount_of_money < 1000:
        if not amount_of_money % banknotes[5]:
            count_500 = amount_of_money // 500
            amount_of_money = 0
        else:
            remainder = amount_of_money % 500
            count_500 = amount_of_money // 500
            amount_of_money = remainder

    elif 200 <= amount_of_money < 500:
        if not amount_of_money % banknotes[4]:
            count_200 = amount_of_money // 200
            amount_of_money = 0
        else:
            remainder = amount_of_money % 200
            count_200 = amount_of_money // 200
            amount_of_money = remainder

    elif 100 <= amount_of_money < 200:
        if not amount_of_money % banknotes[3]:
            count_100 = amount_of_money // 100
            amount_of_money = 0
        else:
            remainder = amount_of_money % 100
            count_100 = amount_of_money // 100
            amount_of_money = remainder

    elif 50 <= amount_of_money < 100:
        if not amount_of_money % banknotes[2]:
            count_50 = amount_of_money // 50
            amount_of_money = 0
        else:
            remainder = amount_of_money % 50
            count_50 = amount_of_money // 50
            amount_of_money = remainder

    elif 20 <= amount_of_money < 50:
        if not amount_of_money % banknotes[1]:
            count_20 = amount_of_money // 20
            amount_of_money = 0
        else:
            remainder = amount_of_money % 20
            count_20 = amount_of_money // 20
            amount_of_money = remainder
    elif 10 <= amount_of_money < 20:
        if not amount_of_money % banknotes[0]:
            count_10 = amount_of_money // 10
            amount_of_money = 0
        else:
            remainder = amount_of_money % 10
            count_10 = amount_of_money // 10
            amount_of_money = remainder

print(f"10 hryvnia banknote: {count_10}")
print(f"20 hryvnia banknote: {count_20}")
print(f"50 hryvnia banknote: {count_50}")
print(f"100 hryvnia banknote: {count_100}")
print(f"200 hryvnia banknote: {count_200}")
print(f"500 hryvnia banknote: {count_500}")
print(f"1000 hryvnia banknote: {count_1000}")
