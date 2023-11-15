"""
File: rotten_tomato.py
Name:
-------------------------------
This file shows basic AI in classification task:
movie review classification.
First, tokenize the review
Second, count each token and give them corresponding scores
Finally, calculate the score for each word such that we can
predict a movie review by summing over the scores
"""


# The file with labels and reviews
FILENAME = 'movie_review.txt'


def main():
	with open(FILENAME, 'r') as f:
		d = {}
		for line in f:
			score, review = line.split(':')
			score = int(score[1:3])
			tokens = review.split()
			for token in tokens:
				token = string_manipulation(token)
				if token not in d:
					d[token] = score
				else:
					d[token] += score


def string_manipulation(string):
	ans = ""
	for ch in string:
		if ch.isalpha():
			ans += ch.lower

	return ans



if __name__ == '__main__':
	main()
