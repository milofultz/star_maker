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

# Vertical Star List Maker - Creates the vertical lists of stars that will span the screen
def star_list_maker():
    # make an empty list to hold all star lists
    star_list = []
    # for the amount of vertical lines in the terminal
    for lines in range(width):
        # make an empty list to hold chars
        char_list = []
        # make a random selection of space, stars, or bodies
        star_line = star_line_maker()
        # for every char in this random selection
        for char in star_line:
            # color the char and add it to the char list
            # char_list.append(star_color(char))
            char_list.append(char)
        # add the char list to the all star list
        star_list.append(char_list)
    # send the list out
    return star_list

def star_line_maker():
    chars = width
    star_line = ''

    # make a random selection of space, stars, or bodies
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
    # make a temp place for the colored char to go
    color_char = ''
    # check to see what kind of a char it is
    if char in ascii_bodies:
        # add color code to temp place with char and end tag
        color_char += bodies_color + char + no_color
    elif random.randint(0,2) == 0:
        color_char += space_color + char + no_color
    else:
        color_char += bold + char + no_color

    # return the new colored char
    return color_char

def star_concatenator(star_list):
    # make a blank list to put all of the finished strings
    star_str_list = []
    # for as many times as there are horizontal lines in the terminal
    for line in range(height-2):
        # make a blank string to add the concatenated elements
        star_str_line = ' '
        # concatenate all of the same numbered elements from every list
        for lst in star_list:
            star_str_line += lst[line]
        star_str_line += ' '
        # add the concatenated string to the list
        star_str_list.append(star_str_line)
    
    star_str = '\n'
    # return the finished list
    for i in star_str_list:
        star_str += i + '\n'
    return star_str

# Star Shifter - Shifts each vertical star list by a regular amount to achieve the parallax effect
def star_shifter(star_list):
    shifted_star_list = star_list

    # for every list in the list
    for num, lst in enumerate(star_list):
        # see if it's part of group 1, 2, or 3
        column = num % 4
        # if it's part of group 1, don't do anything
        if column == 0:
            shifted_star_list[num] = lst[-1:] + lst[:-1]
        # if it's part of group 2, shift all of it's elements by 1
        if column == 1:
            shifted_star_list[num] = lst[-2:] + lst[:-2]
        # if it's part of group 3, shift all of it's elements by 2
        if column == 2:
            shifted_star_list[num] = lst[-3:] + lst[:-3]
        if column == 3:
            shifted_star_list[num] = lst[-4:] + lst[:-4]
    # return the list of shifted lists
    return shifted_star_list


if __name__ == '__main__':
    with TERM.hidden_cursor():
        star_list = star_list_maker()
        star_str = star_concatenator(star_list)
            
        while True:
            print(star_str)
            star_list = star_shifter(star_list)
            star_str = star_concatenator(star_list)
            sleep(.4)