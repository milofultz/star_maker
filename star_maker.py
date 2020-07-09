#star maker

import random
from time import sleep

from blessed import Terminal

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


def random_nothing():
    string = ' '
    number = random.randint(1,40)
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
    chars = width*4
    space = ''

    for i in range(chars):
        nothing = random_nothing()
        star = pick_star(char_lst, spec_char_lst)
        space += (nothing + star)

    return space

def convert_to_list(stars, width):
    line = width

    stars_lst = [stars[i:i+line] for i in range(0, len(stars), line)]

    return stars_lst

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

def scroller(stars_lst, height=24):
    with TERM.hidden_cursor():
        star_screen = ''
        for line in stars_lst:
        	star_screen += line
        print(star_screen) #to clear screen

        while True:
            random.shuffle(stars_lst)
            for i in range(2*height):
                print(stars_lst[i])
                sleep(.75)


if __name__ == '__main__':

    stars_str = make_space(ascii_space, ascii_bodies)
    stars_lst = convert_to_list(stars_str, width)
    color_stars_lst = make_colorful(stars_lst)

    scroller(color_stars_lst, height)