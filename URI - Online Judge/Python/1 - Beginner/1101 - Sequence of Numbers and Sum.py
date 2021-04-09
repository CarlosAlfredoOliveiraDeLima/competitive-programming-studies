M, N = map(int, input().split(' '))

while M > 0 and N > 0:
    string = ''
    soma = 0
    if M > N:
        M, N = N, M

    for i in range(M, N+1):
        string += f'{i} '
        soma += i
    print(f'{string}Sum={soma}')
    M, N = map(int, input().split(' '))
