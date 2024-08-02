import random, subprocess, time

def main_menu():
    print('В какую игру будем играть?')
    rock_paper_scissor = input('Камень, ножницы, бумага? + или -: ')
    if rock_paper_scissor == '+':
        rock_paper_scissors()
        main_menu()
    elif rock_paper_scissor == '-':
        guess_the_numbe = input('Угадай число? + или -: ')
        if guess_the_numbe == '+':
            guess_the_number()
            main_menu()
        elif guess_the_numbe == '-':
            main_menu()
        else:
            print('Вы неверно ответили😟.')
            main_menu()
    
    else:
        filename = time.strftime("file_%Y-%m-%d_%H-%M-%S.log")
        subprocess.run(['df', '-h'], stdout=open(filename, 'w'))


def rock_paper_scissors():
    print('Если захотите закончить вводите стоп.')
    print('Если захотите узнать счёт вводите счёт.')
    user_ball = 0
    rand_ball = 0
    while True:
        user = input("Камень, ножницы или бумага? (Вводите камень, ножницы или бумага): ")
        list_play = ['камень', 'ножницы', 'бумага']
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)

            if rand == 'камень' and user == 'ножницы':
                rand_ball += 1
            if rand == 'камень' and user == 'бумага':
                user_ball += 1
            if rand == 'ножницы' and user == 'камень':
                user_ball += 1
            if rand == 'ножницы' and user == 'бумага':
                rand_ball += 1
            if rand == 'бумага' and user == 'ножницы':
                user_ball += 1
            if rand == 'бумага' and user == 'камень':
                rand_ball += 1
        elif user == 'счёт':
            print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")
        elif user == 'стоп':
            print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")
            print('Конец игры! Заходите ещё!')
            break
        else:
            print('Вводите камень, ножницы или бумага.')


def guess_the_number():
    start = 1
    finish = 101
    count = 1
    while True:
        size = (start + finish) // 2
        print('Твоё число равно, меньше или больше, чем число', size,'?')
        answer = int(input('Ответь если 1 - равно, 2 - меньше, 3 - больше: '))
        count += 1
        if answer == 1:
            print('Я угадал! с ', count, 'попытки')
            break
        if answer == 2:
            finish = size
        else:
            start = size

main_menu()