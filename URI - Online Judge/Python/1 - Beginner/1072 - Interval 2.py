numbers = int(input())
numbersIn = 0
numbersOut = 0

for i in range(numbers):
    aux = int(input())
    if 10 <= aux <= 20:
        numbersIn += 1
    else:
        numbersOut += 1

print(f'{numbersIn} in')
print(f'{numbersOut} out')
