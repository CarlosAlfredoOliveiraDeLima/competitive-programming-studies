positive_Numbers = 0

for i in range(6):
    number = float(input())
    positive_Numbers += 1 if number > 0 else 0

print(f'{positive_Numbers} valores positivos')
