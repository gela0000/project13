"""
File: coin_flip_runs.py
Name: Angela
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO: Generates random "H" or "T" and stop until reaching the number of runs set by the user.
	"""
	count = 0  # keep track of numbers of continuous "H"s or "T"s

	print("Let's flip a coin!")
	num = int(input("Numbers of runs: "))
	letter = r.choice("HT")
	while count < num:
		print(letter, end="")
		if letter == "H":
			letter = r.choice("HT")
			if letter == "H":  # continuous "H"
				count += 1
				while letter == "H":
					print(letter, end="")
					letter = r.choice("HT")
		elif letter == "T":
			letter = r.choice("HT")
			if letter == "T":  # continuous "T"
				count += 1
				while letter == "T":
					print(letter, end="")
					letter = r.choice("HT")
# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()

