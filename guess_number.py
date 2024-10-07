from random import randint
number = randint(1, 100)
print('Угадайте число от 1 до 100')

def guess_wow_wow():

    while True:
        guess_wow = int(input(' Ввидите число: '))

        if guess_wow < number:
            print('Ваше число меньше загаданного')

        elif guess_wow > number:
            print('Ваше число больше загаданного')

        else:
            break

    print('Отличная интуиция! Вы угадали число:)')  
guess_wow_wow()