# Банкомат выдает купюры номиналом 10 и 20 гривен (не более десяти купюр каждого номинала).
# Однако если банкомат выдал максимум десяток и двадцаток,
# то остальные деньги он выдает пятидесятками (без ограничения количества).

try:
    val = int(input("The ATM issues banknotes of 10 and 20 hryvnia (no more than 10 of each denomination). \n"
                    "However, if the ATM issued a maximum of tens and twenties, then it issues the rest of the money "
                    "in fifties (without limit)  \n\nEnter the amount of money what do you want to receive:"))

    count = 0
    count10 = 0
    count20 = 0
    count50 = 0
    num = val

    if val > 0 and not val % 10:
        while val:
            if count < 10:
                count10 += 1
            else:
                l = num - count10 * 10
                if not l % 20:
                    for x in range(l // 20):
                        if x < 10:
                            count20 += 1
                    val = 0

                elif l % 20:
                    if not (l + 10) % 20:
                        for x in range(l // 20):
                            if x < 10:
                                count20 += 1

                        if count20 < 10:
                            count10 -= 1
                        if count20 < 10:
                            count20 += 1
                        val = 0

                if (not val) and (count20 >= 10):
                    l = num - (count20 * 20 + count10 * 10)

                    if not l % 50 and count50 < 10:
                        for x in range(l // 50):
                            count50 += 1

                    elif l % 50 and count50 < 10:
                        if not ((l - 10) % 50):
                            for x in range(l // 50):
                                count50 += 1
                            count50 += 1
                            count20 -= 2
                        elif not (l - 20) % 50:
                            for x in range(l // 50):
                                count50 += 1
                            count50 += 1
                            count10 -= 1
                            count20 -= 1
                        elif not (l - 30) % 50:
                            for x in range(l // 50):
                                count50 += 1
                            count50 += 1
                            count20 -= 1
                        elif not (l - 40) % 50:
                            for x in range(l // 50):
                                count50 += 1
                            count50 += 1
                            count10 -= 1

            if val:
                val -= 10

            count += 1

        print(f"10 hryvnia banknote: {count10}")
        print(f"20 hryvnia banknote: {count20}")
        print(f"50 hryvnia banknote: {count50}")

    else:
        print(f"You are entered a negative number or number not divisible by 10")

except Exception as e:
    print(e)
