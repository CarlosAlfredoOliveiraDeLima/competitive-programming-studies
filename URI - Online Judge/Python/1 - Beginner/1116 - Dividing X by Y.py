quantity_of_pairs = int(input())

for i in range(quantity_of_pairs):
    X, Y = map(int, input().split(' '))

    try:
        print(f'{(X / Y):.1f}')
    except ZeroDivisionError:
        print('divisao impossivel')
