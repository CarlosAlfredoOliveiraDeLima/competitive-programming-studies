def quadrante(x, y):
    if x > 0 < y:
        return 'primeiro'
    elif x > 0 > y:
        return 'quarto'
    elif x < 0 > y:
        return 'terceiro'
    else:
        return 'segundo'


while True:
    n1, n2 = map(int, input().split())
    if n1 == 0 or n2 == 0:
        break
    print(quadrante(n1, n2))
