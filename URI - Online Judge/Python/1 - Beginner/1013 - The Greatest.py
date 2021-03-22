a, b, c = map(int, input().split(' '))

maior = (a + b + abs(a-b)) / 2
maior = int((maior + c + abs(maior - c)) / 2)

print(f'{maior} eh o maior')
