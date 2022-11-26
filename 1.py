# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input('Введитн число ')
sumn = 0
for i in number:
    if i.isdigit():
        sumn += int(i)
print(f'Сумма цифр = {sumn}')