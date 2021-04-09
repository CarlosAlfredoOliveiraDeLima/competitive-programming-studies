N = int(input())
for i in range(N):
    number = int(input())
    if number == 0:
        print('NULL')
    elif number % 2 == 0:
        if number > 0:
            print('EVEN POSITIVE')
        else:
            print('EVEN NEGATIVE')
    elif number % 2 != 0:
        if number > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')
