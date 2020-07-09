#parallax v2
from blessed import Terminal

import random
from time import sleep

TERM = Terminal()

ascii_space = ['"', "'", '.', ',', '`', '+', '˜', '˚', '¨', 'ˆ', '“', '‘', '¸', '˛']
ascii_bodies = ['ø', '°', '*', '~', '%', 'c', 'O', '0', '?', '©', '∆', '®', '«', '◊', '', '‰', 'Œ']

space_colors = [ TERM.white, TERM.bright_white, TERM.yellow, TERM.bright_black ]
bodies_colors = [ TERM.red, TERM.green, TERM.yellow, TERM.blue, TERM.magenta,
    TERM.cyan, TERM.white, TERM.bright_black, TERM.bright_red, 
    TERM.bright_green, TERM.bright_yellow, TERM.bright_blue, 
    TERM.bright_magenta, TERM.bright_cyan, TERM.bright_white ]
bold = TERM.bold
no_color = TERM.normal
width = TERM.width-2
height = TERM.height-2


def star_list_maker():
    star_list = []

    for lines in range(width):
        char_list = []

        star_line = star_line_maker()
        for char in star_line:
            char_list.append(star_color(char)) #color version
            # char_list.append(char) #b&w version if using iTerm
        star_list.append(char_list)

    return star_list

def star_line_maker():
    chars = width
    star_line = ''

    for i in range(chars*8):
        if len(star_line) >= width*8:
            break
        elif i % 2:
            star_line += pick_star()
        else:
            star_line += random_nothing()

    return star_line[width:width*7]

def random_nothing():
    string = ' '

    number = random.randint(0,100)
    string = string * number

    return string

def pick_star():
    prob = random.randint(0, width//2)

    if prob == 1: #lower probability
        star = random.choice(ascii_bodies)
    else:
        star = random.choice(ascii_space)

    return star

def star_color(char):
    bodies_color = random.choice(bodies_colors)
    space_color = random.choice(space_colors)
    color_char = ''

    if char in ascii_bodies:
        color_char += bodies_color + char + no_color
    elif random.randint(0,2) == 0:
        color_char += space_color + char + no_color
    else:
        color_char += bold + char + no_color

    return color_char

def star_concatenator(star_list):
    star_str_list = []

    for line in range(height-2):
        star_str_line = ' '
        for lst in star_list:
            star_str_line += lst[line]
        star_str_line += ' '
        star_str_list.append(star_str_line)
    
    star_str = '\n'
    for i in star_str_list:
        star_str += i + '\n'
    return star_str

def star_shifter(star_list):
    shifted_star_list = star_list

    for num, lst in enumerate(star_list):
        column = num % 4

        if column == 0:
            shifted_star_list[num] = lst[-1:] + lst[:-1]
        if column == 1:
            shifted_star_list[num] = lst[-2:] + lst[:-2]
        if column == 2:
            shifted_star_list[num] = lst[-3:] + lst[:-3]
        if column == 3:
            shifted_star_list[num] = lst[-4:] + lst[:-4]

    return shifted_star_list


if __name__ == '__main__':
    with TERM.hidden_cursor():
        star_list = star_list_maker()
        star_str = star_concatenator(star_list)
            
        while True:
            print(star_str)
            star_list = star_shifter(star_list)
            star_str = star_concatenator(star_list)
            sleep(.25)