number1 = int(input())
number2 = int(input())

if number1 > number2:
    number1, number2 = number2, number1

sumOfOddNumbers = 0
for i in range(number1+1, number2):
    sumOfOddNumbers += i if i % 2 != 0 else 0

print(sumOfOddNumbers)
