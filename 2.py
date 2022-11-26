# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

n = int(input("Введите чисто "))
numbers = [1]
for i in range(2, n+1):
    numbers.append(numbers[-1] * i)
print(numbers)