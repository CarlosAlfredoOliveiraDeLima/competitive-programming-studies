max_number = 0
position = 0
for i in range(1, 101):
    aux = int(input())
    if aux > max_number:
        max_number = aux
        position = i
print(max_number)
print(position)


'''
numbers = []
for i in range(100):
    numbers.append(int(input()))

print(max(numbers))
print(numbers.index(max(numbers)) + 1)
'''

