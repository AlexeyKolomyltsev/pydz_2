# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

n = int(input("Введите число "))
chain = []
sumn = 0
for i in range(1 , n+1):
    manipulation_num = round((1 + 1/i)**i, 2)
    chain.append(manipulation_num)
    sumn += manipulation_num
print(chain, sumn, sep='\n')