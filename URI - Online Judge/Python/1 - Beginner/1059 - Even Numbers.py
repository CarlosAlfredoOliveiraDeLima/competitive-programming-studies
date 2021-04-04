def evenNumber(x):
    if x % 2 == 0:
        return x


for i in [x for x in list(map(evenNumber, [x for x in range(1, 101)])) if x is not None]:
    print(i)
