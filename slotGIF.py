'''
Program: slotGIF.py
Author: Amit
Date: 9/22/19

Program uses gui with GIFs to imitate a slot machine 
which generates three random GIFs from a list.  If all 
three GIFs match, then user wins grand prize. If two 
out of three match, then user wins second prize.
'''

from breezypythongui import EasyFrame
import random
from tkinter import PhotoImage
from tkinter.font import Font 

class SlotGIF(EasyFrame):

	def __init__(self):
		''' sets up the window and the widgets'''
		EasyFrame.__init__(self, "Lotsa Slots", width = 600, height = 450, background = 'powderblue')

		# sets up the labels and widgets
		self.title = self.addLabel(text = "Ready to Play?", row = 0, column = 0, columnspan = 3, sticky = "NSEW", background = 'powderblue', font = ("Helvetica", 20, 'italic'))
		self.image1 = self.addLabel(text = "", row = 1, column = 0, rowspan = 2, sticky = "NSEW", background = 'powderblue')
		self.image2 = self.addLabel(text = "", row = 1, column = 1, rowspan = 2, sticky = "NSEW", background = 'powderblue')
		self.image3 = self.addLabel(text = "", row = 1, column = 2, rowspan = 2, sticky = "NSEW", background = 'powderblue')

		self.main = self.addLabel(text = "Let's Make Some Magic Baby", row = 3, column = 0, columnspan = 3, sticky = "NSEW", background = 'powderblue', font = ("Arial Black", 20))
		self.button = self.addButton(text = "Spin That Shit", row = 4, column = 0, columnspan = 4, command = self.spin)
		self.addLabel(text = "", row = 5, column =0, columnspan = 4, sticky = "NSEW", background = 'powderblue')

		self.button["background"] = 'red'
		self.button["foreground"] = 'white'
		self.button["font"] = "Times+New+Roman"


	def spin(self):

		# Loads the images and associates them with variables
		self.image = PhotoImage(file = "smokey.gif")
		self.fly = PhotoImage(file = "fly.gif")
		self.really = PhotoImage(file = "really.gif")
		
		# Array of images
		master = [self.image, self.fly, self.really]

		# Randomly generate image from list and assign a variable
		one = random.choice(master)
		two = random.choice(master)
		three = random.choice(master)
	
		# Load variable image into labels
		self.image1["image"] = one
		self.image2["image"] = two
		self.image3["image"] = three

		# Game mechanics for deciding if there is a winner or not
		if one == two == three:
			self.win = self.addLabel(text = "YOU JUST WON, BIIIIIIG TIME!!", row = 5, column = 0, columnspan = 4, sticky = "NSEW", background = 'yellow', font = ("Arial+Bold", 22, 'italic'))
		elif one == two or one == three or two == three:
			self.runner = self.addLabel(text = "YOU WIN... JUST IN SECOND PLACE!", row = 5, column = 0, columnspan = 4, sticky = "NSEW", background = 'lawngreen', font = ("Verdana", 18))
		else:
			self.nowin = self.addLabel(text = "WOMP WOMP, SPIN AGAIN", row = 5, column =0, columnspan = 4, sticky = "NSEW", background = 'powderblue', font = ("Helvetica", 14, 'bold'))


def main():
	SlotGIF().mainloop()

main()
