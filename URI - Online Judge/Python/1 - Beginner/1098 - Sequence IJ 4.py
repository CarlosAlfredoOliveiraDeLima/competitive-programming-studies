I = 0
l = 0
h = 1
while I <= 2:
    J = 1
    J = J + l
    for k in range(1, 4):
        print(f'I={I:.0f} J={J:.0f}') if h == 1 or h == 6 or h == 11 else print(f'I={I:.1f} J={J:.1f}')
        J += 1
    I += 0.2
    l += 0.2
    h += 1
    
'''
i = 0
j = 1

while(i != 2.2):
    print('I=%s J=%s' % (i, j))
    j = j + 1
    if(j == (i + 4)):
        i = round(i + 0.2, 1)
        j = round(j - 2.8, 1)
'''