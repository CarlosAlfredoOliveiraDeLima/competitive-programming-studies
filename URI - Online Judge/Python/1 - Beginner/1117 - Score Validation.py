number_of_valid_scores = 0
average = 0
while number_of_valid_scores < 2:
    score = float(input())

    if 0 <= score <= 10:
        average += score
        number_of_valid_scores += 1
    else:
        print('nota invalida')

print(f'media = {(average/2):.2f}')
