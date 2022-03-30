continue_inspection = True

while continue_inspection == True:
    average = 0
    number_valid_score = 0
    while number_valid_score < 2:
        score = float(input())

        if 0 <= score <= 10:
            average += score
            number_valid_score += 1
        else:
            print('nota invalida')

    print(f'media = {(average/2):.2f}')
    
    
    new_inspection = 3
    while new_inspection != 1 and new_inspection != 2:
        new_inspection = int(input('novo calculo (1-sim 2-nao)\n'))
        if new_inspection == 1:
            continue_inspection = True
        elif new_inspection == 2:
            continue_inspection = False