#star maker

import random
from time import sleep

from blessed import Terminal

TERM = Terminal()

ascii_space = ['"', "'", '.', ',', '`', '+']
ascii_bodies = ['ø', '°', '*', '~']

def random_nothing():
    string = ' '
    number = random.randint(0,30)
    string = string * number

    return string

def pick_star(char_lst, spec_char_lst):
    random.shuffle(char_lst)
    random.shuffle(spec_char_lst)
    d_100 = random.randint(0,100)

    if d_100 == 1: #lower probability
        star = spec_char_lst[0]
    else:
        star = char_lst[0]

    return star

def make_space(char_lst, spec_char_lst):
    chars = 10000
    space = ''

    for i in range(chars):
        nothing = random_nothing()
        star = pick_star(char_lst, spec_char_lst)
        space += (nothing + star)

    return space

def convert_to_list(stars, width):
    line = width

    star_line = [stars[i:i+line] for i in range(0, len(stars), line)]

    return star_line

def scroller(stars_lst, stars_str, height=24):
    with TERM.hidden_cursor():
        star_screen = TERM.bold(stars_str)
        print(star_screen) #to clear screen

        while True:
            random.shuffle(stars_lst)
            for i in range(2*height):
                star_line = TERM.bold(stars_lst[i])
                print(star_line)
                sleep(.75)


if __name__ == '__main__':
    width = TERM.width
    height = TERM.height

    stars_str = make_space(ascii_space, ascii_bodies)
    stars_lst = convert_to_list(stars_str, width)

    scroller(stars_lst, stars_str, height)