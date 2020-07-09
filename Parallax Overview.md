# Star Maker - Parallax Feature Overview
---

**Describe what your program will do in abstract terms, as if it was a person doing it, not a computer.**

Program will display ASCII on the screen like stars. As time goes on, certain stars will go faster while others go slower to simulate a parallax effect.

**From there, describe how your program will handle data. Start BIG as possible.**

IN: None
OUT: Display of stars

**Break down the process further in abstract terms. What are the distinct actions it will need to take? What would a random stupid guy need if you wanted him to do it?**

- Program begins by opening lists of character types
- Program finds out how big your screen is
- Program makes some lists of stars and space based on these elements
- Program adds color to the list elements
- Program concatenates horizontal strings based on these vertical lists
- Program displays strings on screen
- Program shifts all vertical lists of stars by regular amounts to emulate parallax
- Program continues concatenating horizontal strings based on these vertical lists and displaying them on screen

**Determine the biggest distinct functions you can perceive in the description you just created.**

Vertical Star List Maker - Creates the vertical lists of stars that will span the screen
Star Color - Colors each star in the vertical lists of stars
Star Concatenator - Creates a display friendly format of the stars
Display - Displays the stars
Star Shifter - Shifts each vertical star list by a regular amount to achieve the parallax effect

**What data types would be best to transfer in between these functions?**

Vertical Star List Maker - Creates the vertical lists of stars that will span the screen
	IN: lists, of acceptable characters
	OUT: lists, of created character patterns
Star Color - Colors each star in the vertical lists of stars
	IN: string, character
	OUT: string, character + blessed colors
Star Concatenator - Creates a display friendly format of the stars
	IN: lists, of created character patters
	OUT: list of strings, horizontal print friendly character patterns
Display - Displays the stars
	IN: list of strings, horizontal print friendly character patterns
	OUT: none (display)
Star Shifter - Shifts each vertical star list by a regular amount to achieve the parallax effect
	IN: lists, of created character patters
	OUT: lists, of created character patters but shifted