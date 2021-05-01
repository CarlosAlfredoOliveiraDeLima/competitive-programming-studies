N = int(input())
for i in range(N):
    number1, number2 = map(int, input().split(' '))

    if number1 > number2:
        number1, number2 = number2, number1

    sumOfOddNumbers = 0
    for j in range(number1+1, number2):
        sumOfOddNumbers += j if j % 2 != 0 else 0
    print(sumOfOddNumbers)
