number = int(input())

number += 0 if number % 2 != 0 else 1

for i in range(number, number+12, 2):
    print(i)


"""
num = int(input())
impares = [n for n in range(num,num+12) if n % 2 != 0]
for n in impares:
    print(n)

"""