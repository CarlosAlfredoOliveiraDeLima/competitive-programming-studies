import math

A, B, C = map(float, input().split(' '))

if A == 0 or ((B ** 2) - 4 * A * C) < 0:
    print('Impossivel calcular')
else:
    R1 = (-B + math.sqrt(((B ** 2) - 4 * A * C))) / (2 * A)
    R2 = (-B - math.sqrt(((B ** 2) - 4 * A * C))) / (2 * A)
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))