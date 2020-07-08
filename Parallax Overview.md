# Star Maker - Parallax Feature Overview
---

**Describe what your program will do in abstract terms, as if it was a person doing it, not a computer.**

The program will show different stars moving at different rates vertically across the screen, like parallax. One column will move 1px per move, another will move 2px, another will move 3px.

**From there, describe how your program will handle data. Start BIG as possible.**

Program will take in lines of stars and organize them to create a parallax effect.
IN: list of strings with blessed colors
OUT: updated list of strings

**Break down the process further in abstract terms. What are the distinct actions it will need to take? What would a random stupid guy need if you wanted him to do it?**

- Program will display a screen full of star lines
- Program will receive a list of lines that were just used
- Program will pull each individual line
- Program will divide the line into segments for the parallax lines
- Program will organize the divisions into the different parallax speeds and put them into different lists that correspond to where they were pulled from
- After going through all the lines, Program will create the next lines to be displayed to create the parallax effect by grabbing each 'star' in order from their corresponding lines
- Program will send all updated lines to be displayed

**Determine the biggest distinct functions you can perceive in the description you just created.**

Display - Print all star lines on screen
Parallaxer - Take in all lines last displayed and make a new set of lines with the parallax effect

**What data types would be best to transfer in between these functions?**

Display - IN: list of star lines, OUT: none (display)
Parallaxer - IN: list of last displayed star lines, OUT: list of star lines with parallax effect

**Make a very rough outline of the program using information from chunking steps. Include only necessary in/out information.**

	#Display - IN: list of star lines, OUT: none (display)
	def display(lst):
		pass

	#Parallaxer - IN: list of last displayed star lines, OUT: list of star lines with parallax effect
	def parallaxer(lst):
		new_lst = []
		return new_lst

**Write out overview for each function as if you were telling a random stupid guy to do it.**

Display:
- Program receives list of stars to display
- Program divides list up and puts them together as a new file
- Program displays this file

Parallaxer:

Sorter:
- Program receives list of all stars to fill screen
- Program divides up the list into it's individual lines
- Program takes each line and splits it up by every 1st, 2nd, or 3rd element
- Program places each of these elements into a dictionary: naming them first after which group it belongs to (1,2,3), and then after the line they came from
- Program outputs the dictionary

Compiler:
- Program receives dictionary of sorted elements
- Program makes a list (finished list) to contain the strings that will be created.
- Program will create 6x as many strings as there are lines in the height of the terminal. 
- In each of these strings, Program will take an element from the dictionary's 1 group, followed by an element from the 2 group, and then from the 3 group and add it to the string, repeating this until the line is as long as the width of the terminal screen.
- Program will add a newline to the end of this sequence and repeat until it has done it as many times as there are lines of height in the terminal.
- When finished with this string, Program will add it to the end of the 'finished list'.
- Program will repeat this sequence until it has created all of the aforementioned strings (6x worth).

**Once the program has been broken down into its most atomistic functions, start writing pseudocode into them to have an idea of what you're going to do.**


Further Chunking
---
		
Look for similarities in between functions and see if there is any process the functions could share. If so, then take that and break it down into it's own function. (e.g. in this program, both the crawler and the input need to take all the links off of a given page)

Testing
---
When you feel it has been broken down fully and the flow of data makes sense, make a basic way to test it as it goes. In Python, this is by adding an ```if __name__ == '__main__':``` section. Start with more pseudocode and continue with it until you feel that you can correctly write out the flow using the functions you've already created.

Start Writing Code
---
Figure out what is the easiest thing to program and test. Go with the pseudocode you've written and start fleshing it out with real functionality. Test each part as you go in the terminal. In the following example, I'll first test that I can open a file and return the contents of the file.

```
# Input: Take bookmark file and turn it into a list of links that the program can use.
# IN: HTML file, OUT: List containing relevant information from bookmarks.
def input(filename):
	#Open the file
	with open(filename, 'r') as f:
		html = f.read()
	#Go through the whole file looking for links
	#Copy down all URLs, titles, and include that
	#you found the link on the bookmarks page.
	#Compile it into a document that can be 
	#handled by the Crawler
	url_list = []
	# return url_list
	return html
	
if __name__ = '__main__':
	print(input('bookmarks.html'))
	
############
Terminal
############

$ python3 bm_crawl.py
<html>
	<head>
	...
	</body>
</html>
$
```
Repeat this process with each element of your code, ensuring that it works exactly as you expect. You don't have to go in a linear fashion, if it is easier or more sensible to jump around.

Don't be afraid to go back to previous steps if you realize further possibilities of chunking or other revisions.

---
References:

1. Mason