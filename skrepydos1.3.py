from colorama import *
import os
from datetime import datetime
import random

init()

lang = 'en'
ver = 'SkrePyDos v 1.3'
c = [
    'red',
    'cyan',
    'yellow',
    'white',
    'black',
    'green',
    'magenta',
    'reset'
] # цвета
MUI = {
    'ru': {
        'help': '''help  Выводит справку о командах
clear  Очищает весь терминал
news Список обноовлений
creators  Создатели
calc  Калькулятор
ver  Версия
time Выводит дату и время
exit  Выход

col  Меняет цвет
colrgb Меняет цвет по RGB
gnum  Игра 'Угадай число' 
6ball Игра 'Шар-шестерка'

lang  Устанавливает язык ОС
        ''',
        'number': 'Число: ',
        'above': 'Больше',
        'less': 'Меньше',
        'win': 'Вы выиграли!',
        'gameover': 'Вы проиграли!',
        'munum': 'Мое число: ',
        'type help':'Напиши help для помощи',
        'creators': '''Skre95  Главный разработчик
GimpNotepad  Помощник разработчика''',
        'colors': 'Цвета: ',
        'color': 'Цвет: ',
        'input_err': 'Ошибка при вводе!',
        'example': 'Пример: ',
        'news': '''1.1: Добавлены новые команды и исправлены баги.
1.2: Добавлен перевод
1.3: Немного изменена команда col и добавлена новая команда''',
        'from': 'От: ',
        'to': 'До: ',
        'langs': 'Языки: ',
        'langset': 'Язык: ',
        'wisl': '(писать только маленькими буквами)',
        'syntax_err': 'Неправильная команда!',
        'yes': 'Да',
        'no': 'Нет',
        'ity': 'Я думаю, да',
        'itn': 'Я думаю, нет',
        'allp': 'Все возможно',
        'mnv': 'Мечтать не вредно',
        'q': 'Вопрос: '
    },
    'en': {
        'help': '''help  Displays help about commands
clear  Clears the entire terminal
news  List of updates
creators  Creators
calc  Calculator
ver  Version
time  Displays date and time
exit  Exit

col  Changes color
colrgb  Changes color by RGB
gnum  Game 'Guess the number'
6ball Game 'Six ball'

lang  Sets OS language
        ''',
        'number': 'Number: ',
        'above': 'Above',
        'less': 'Less',
        'win': 'You win!',
        'gameover': 'Game over!',
        'munum': 'My number: ',
        'type help':'Type help for help about commands',
        'creators': '''Skre95  Chief developer
GimpNotepad  Developer Assistant ''',
        'colors': 'Colors: ',
        'color': 'Color: ',
        'input_err': 'Input error!',
        'example': 'Example: ',
        'news': '''1.1: Added new commands and fixed  bugs.
1.2: Translation added
1.3: Slightly changed the col command and added a new command''',
        'from': 'From: ',
        'to': 'To: ',
        'langs': 'Languages: ',
        'langset': 'Language: ',
        'wisl': '(write in small letters only)',
        'syntax_err': 'Syntax error!',
        'yes': 'Yes',
        'no': 'No',
        'ity': 'I think, yes',
        'itn': 'I think, no',
        'allp': 'All is possible',
        'mnv': 'There is no harm in dreaming',
        'q': 'Question: '
    }
}

num = 0

def langt(text, lang=lang):
    return MUI.get(lang, {}).get(text, text)

def sball():
    sixball = [
        langt('yes', lang),
        langt('no', lang),
        langt('ity', lang),
        langt('itn', lang),
        langt('allp', lang),
        langt('mnv', lang)
    ]
    print(sixball[random.randint(0, 5)])


def guess_number():
    for i in range(5) :
        imnum = int(input(langt('number', lang)))
        if imnum < num :
            print(langt('above', lang))
        elif imnum > num :
            print(langt('less', lang))
        else :
            print(langt('win', lang))
            break
    if imnum != num:
        print(langt('gameover', lang))
        print(langt('munum', lang), num)

print(r'''     _____ _    _ _____ ______ _____ _     _ ______   _______ _____
    M  ___| A / /|  __ |  __P_|  __ | |   | |  _I_ \ |  N__  |  ___|
    | |___| |/ / |   __| |____|  ___| |_L_| | |   \ \| |   | | |__X
    |___  |   |  X | \ |  ____| |   |_____  | |    | | |   | |___  |
     ___| | |\ \ | |\ \| |____| Y    _____| | |___/ /| |___U |___| |
    |_____|_| \_\|_| \_\______|_|   |_______|______/ |_______|_____|''', Fore.GREEN, 'v.1.3', Style.RESET_ALL)
print()
print(langt('type help', lang))

while True:
    cmd = input('> ')
    if cmd == 'help':
        print(langt('help', lang))
    elif cmd == 'col':
        print(langt('colors', lang), Fore.RED, 'red,', Fore.CYAN ,' cyan,', Fore.YELLOW, ' yellow,', Fore.WHITE, ' white, ', Back.WHITE, Fore.BLACK, 'black,', Back.RESET, Fore.GREEN, ' green,', Fore.MAGENTA, ' magenta,', Fore.RESET, ' reset', langt('wisl', lang))
        colr = input(langt('color', lang))
        if colr == c[0]:
            print(Fore.RED)
        elif colr == c[1]:
            print(Fore.CYAN)
        elif colr == c[2]:
            print(Fore.YELLOW)
        elif colr == c[3]:
            print(Fore.WHITE)
        elif colr == c[4]:
            print(Fore.BLACK)
        elif colr == c[5]:
            print(Fore.GREEN)
        elif colr == c[6]:
            print(Fore.MAGENTA)
        elif colr == c[7]:
            print(Fore.RESET)
        else:
            print(langt('input_err', lang))
    elif cmd == 'clear':
        os.system('cls')
    elif cmd == 'calc':
        primer = input(langt('example', lang))
        try:
            r = eval(primer)
            print(primer, '=', r)
        except:
            print(langt('input_err', lang))
    elif cmd == 'ver':
        print(ver)
    elif cmd == 'exit':
        break
    elif cmd == 'time':
        t = datetime.now()
        print(t.strftime("%Y-%m-%d %H:%M:%S"))
    elif cmd == 'news':
        print(langt('news', lang))
    elif cmd == 'creators':
        print(langt('creators', lang))
    elif cmd == 'colrgb':
        r = input('r: ')
        g = input('g: ')
        b = input('b: ')
        print('\033[38;2;' + r + ';'+ g + ';' + b + 'm')
    elif cmd == 'gnum':
        try:
            ot = int(input(langt('from', lang)))
            do = int(input(langt('to', lang)))
            num = random.randint(ot, do)
            guess_number()
        except:
            print(langt('input_err', lang))
    elif cmd == 'lang':
        print(langt('langs', lang), 'ru, en.')
        l = input(langt('langset', lang))
        if l == 'ru' or l == 'en':
            lang = l
        else:
            print(langt('input_err', lang))
    elif cmd == '6ball':
        input(langt('q', lang))
        sball()
    else:
        print(langt('syntax_err', lang))

exit()