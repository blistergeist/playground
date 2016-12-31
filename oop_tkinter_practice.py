# oop_tkinter_practice.py
import tkinter as tk

class app(tk.Tk):
	def __init__(self, *args, **kwargs):
		# *args passing any number of arguments
		# **kwargs passing any number of "dictionaries"
		tk.Tk.__init__(self, *args, **kwargs)
		
		# container
		container = tk.Frame(self)

		# pack vs grid
		container.pack(side='top', fill='both', expand=True)


class One:
	def __init__(self):
		self.yar = 'yar'
		self.dingus = 506

	def one_print(self):
		print(self.yar)
		print(self.dingus)

class Two(One):
	def __init__(self):
		super().__init__()
		self.plink = 'plink'
		self.boing = 444

	def two_print(self):
		print(self.plink)
		print(self.boing)

def main():
	one = One()
	one.one_print()
	two = Two()
	two.one_print()
	two.two_print()

if __name__ == '__main__':
	main()