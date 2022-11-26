# Реализуйте алгоритм перемешивания списка.
import random

def mix_chain(chain):
    new_chain = []
    while len(chain) > 1:
        new_chain.append(chain.pop(random.randint(0, len(chain) - 1)))
    new_chain.append(chain.pop())
    return new_chain


n = int(input("Введите размер списка "))
chain = list(
    map(int, input(f'Введите через пробел {n} элемента(-ов) списка ').split(' ')))
print(chain)


print(mix_chain(chain))