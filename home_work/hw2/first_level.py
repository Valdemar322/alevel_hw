#############################################################################
print("Give it to me!")
number = int(input())

if (number >= 100):
    print("Thanks, man!")
elif ((number > 10) and (number < 100)):
    print("OK :(")
else:
    print("WHAAAAT????")

if (number > 1000):
    print("!!!!WOOOOWWWW!!!")
#############################################################################
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)  # True
print(l1 is l2)  # False
print(l1 is not l2)  # True
#############################################################################
l1 = [1, 2, 3]
print(3 in l1)  # True
print(4 in l1)  # False
print(5 not in l1)  # True
#############################################################################
x = 5
y = 10
z = 15

print((x < y) and (y <= z))  # True
print(x < y <= z)  # True
#############################################################################
data = [True, True, True, True]
result = all(data)
print(result)  # Output: True
#############################################################################
data = [False, False, True, False]
result = any(data)
print(result)  # Output: True
#############################################################################
test = True
result = 'Test is true' if test else 'Test is false'
print(result)  # Test is true
#############################################################################
test = True
print('ttt' if test else 'fff')  # ttt
#############################################################################
# test = True
# result = 'Test is True' if test else pass  # Данная строка вызывает ошибку SyntaxError
# print(result) # result = 'Test is True'
#############################################################################
s = ''
if s:
    pass
if 8 % 2:
    pass
#############################################################################
test = True
result = test and 'Test is True' or 'Test is False'
print(result)  # Test is True
