from random import randint
number = randint(1, 100)
print('Угадайте число от 1 до 100')

def guess_number():

    while True:
        guess = int(input(' Ввидите число: '))

        if guess < number:
            print('Ваше число меньше загаданного')

        elif guess > number:
            print('Ваше число больше загаданного')

        else:
            break

    print('Отличная интуиция! Вы угадали число:)')  
guess_number()