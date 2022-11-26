# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.

n = int(input("Введите число "))
chain = list(range(-n, n+1))
print(chain)
index_position = list(map(int, input(f'Введите через пробел 3 индекса от 0 до {n * 2} ').split(' ')))
print(index_position)
multiple = 1
for i in index_position:
    multiple *= chain[i]

print(f'{chain[index_position[0]]} * {chain[index_position[1]]} * {chain[index_position[2]]} = {multiple}')