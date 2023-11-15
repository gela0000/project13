"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'romeojuliet.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
	word_d = {}
	with open(FILE, 'r') as f:
		for line in f:
			tokens = line.split()
			for token in tokens:
				token = token_manipulation(token)
				if token not in word_d:
					word_d[token] = 1
				else:
					word_d[token] += 1
		print_out_d(word_d)


def print_out_d(d):
	"""
	: param d: (dict) key of type str is a word
					value of type int is the word occurrence
	---------------------------------------------------------------
	This function prints out all the info in d
	"""
	for key, value in sorted(d.items(), key=lambda t : t[1]):
		print(key, '-->', value)


def token_manipulation(token):
	ans = ''
	for ch in token:
		if ch.isalpha() or ch.isdigit():
			ans += ch.lower()
	return ans

if __name__ == '__main__':
	main()
