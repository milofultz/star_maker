#parallax ideas
from blessed import Terminal

import random

TERM = Terminal()

ascii_space = ['"', "'", '.', ',', '`', '+', ';', '˜', '˚', '¨', 'ˆ', '“', '‘', '¸', '˛']
ascii_bodies = ['ø', '°', '*', '~', '%', 'c', 'O', '0', '?', '©', '∆', '®', '«', '◊', '', '‰', 'Œ']

space_colors = [ TERM.white, TERM.bright_white, TERM.yellow, TERM.bright_black ]
bodies_colors = [ TERM.red, TERM.green, TERM.yellow, TERM.blue, TERM.magenta,
    TERM.cyan, TERM.white, TERM.bright_black, TERM.bright_red, 
    TERM.bright_green, TERM.bright_yellow, TERM.bright_blue, 
    TERM.bright_magenta, TERM.bright_cyan, TERM.bright_white ]
bold = TERM.bold
no_color = TERM.normal
width = TERM.width
height = TERM.height

# This makes a new line of stars the width of the terminal
def make_space():
    space_lst = [make_space_line() for i in range(height)]
    # for i in range(height):
    #   space_lst.append(make_space_line())

    colorful_space_lst = make_colorful(space_lst)

    return colorful_space_lst

def make_space_line():
    chars = width
    space_line = ''

    for i in range(chars):
        nothing = random_nothing()
        star = pick_star()
        space_line += (nothing + star)

    return space_line

def make_colorful(stars_lst):
    color_stars_lst = []

    for line in stars_lst:
        color_stars_line = ''
        for char in line:
            random.shuffle(bodies_colors)
            bodies_color = bodies_colors[0]
            random.shuffle(space_colors)
            space_color = space_colors[0]
            if char in ascii_bodies:
                color_stars_line += bodies_color + char + no_color
            elif random.randint(0,2) == 0:
                color_stars_line += space_color + char + no_color
            else:
                color_stars_line += bold + char + no_color
        color_stars_lst.append(color_stars_line)

    return color_stars_lst

def random_nothing():
    string = ' '
    number = random.randint(1,40)
    string = string * number

    return string

def pick_star():
    prob = random.randint(0, width//2)

    if prob == 1: #lower probability
        star = random.choice(ascii_bodies)
    else:
        star = random.choice(ascii_space)

    return star

# This takes what was just displayed and adds a new line at the bottom to make the parallax work. Use 'make_stars()'
def starting_stars(new_line, stars):
    stars.pop(0)
    stars.append(new_line)
    # Returns a list of strings, width the same as the terminal
    return stars

# Separates the list line-by-line and feeds it into the char_grouper. Separates each character group into its own list and returns that.
def list_formatter(space):
    formatted_space = []
    for line in space:
        formatted_space.append(char_grouper(line))

    return formatted_space

#this clumps together formatting and characters so that counting width will work
def char_grouper(space):
    
    form_char_lst = []
    form_on = False
    form_char = ''

    for char in space:
        if len(char) != (1 or 0) and form_on == False:
            form_char += char
            form_on = True
        elif len(char) != (1 or 0) and form_on == True:
            form_char += char
            form_on = False
            form_char_lst.append(form_char)
            form_char = ''
        elif len(char) == (1 or 0) and form_on == False: #if it's just a normal character or space
            form_char_lst.append(char)
        elif len(char) == (1 or 0) and form_on == True:
            form_char += char

    return form_char_lst


if __name__ == '__main__':
    stars_lst = make_space()