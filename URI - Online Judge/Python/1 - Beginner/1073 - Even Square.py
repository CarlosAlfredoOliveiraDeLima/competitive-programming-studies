N = int(input())

for i in range(2, N+1):
    if i % 2 == 0:
        print(f'{i}^2 = {pow(i, 2)}')
