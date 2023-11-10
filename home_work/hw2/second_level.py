# first example
try:
    user_number = int(input("Enter some number: "))
    if user_number > 0:
        print("You are entered a positive number")
    elif user_number < 0:
        print("You are entered a negative number")
    else:
        print("You are entered 0")
except Exception as e:
    print(e)

# second example
try:
    user_number1 = int(input("Enter first number: "))
    user_number2 = int(input("Enter second number: "))
    if user_number2:
        print(f"{user_number1}:{user_number2} = {user_number1 / user_number2}")
    else:
        print("You can not divide by zero!")
except Exception as e:
    print(e)

# third example

# Выведет 5 т.к. оператор and ищет последнее правдивое выражение пока на его пути не встретится False и оператор and
# имеет выше приоритет чем or, т.е.
# 1 правда, идет дальше и так до 5, потом идет оператор or, который ищет первое правдивое выражение, в данном примере
# это 5, т.к. сравнивается 5 и результат выполнения 10 and 1 and 2, которые выдают 2 и в итоге остается 5 or 2 и or
# выбирает первое правдивое выражение, т.е. 5
print(1 and 2 and 3 and 4 and 5 or 10 and 1 and 2)
