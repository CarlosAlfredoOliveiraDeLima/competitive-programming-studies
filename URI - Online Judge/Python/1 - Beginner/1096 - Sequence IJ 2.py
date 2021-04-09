[print(f'I={I} J={J}') for I in range(1, 10, 2) for J in range(7, 4, -1)]

"""
for I in range(1, 10, 2):
    for J in range(7, 4, -1):
        print(f'I={I} J={J}')
"""

"""
for I in range(1, 10, 2):
    J = 7
    for k in range(3):
        print(f'I={I} J={J}')
        J -= 1
"""