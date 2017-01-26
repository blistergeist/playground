# around.py
from nltk import word_tokenize
from math import log

def around(document, word1, word2, range=20, matchCase=False):
	if matchCase == False:
		word1 = word1.lower()
		word2 = word2.lower()
		document = document.lower()
	tokens = word_tokenize(document)
	idx1 = []
	idx2 = []
	for i, j in enumerate(tokens):
		if j == word1:
			idx1.append(i)
		if j == word2:
			idx2.append(i)
	prob1 = len(idx1)
	prob2 = len(idx2)

	prob12 = 0
	for w1 in idx1:
		for w2 in idx2:
			if abs(w1-w2) < range:
				prob12 +=1
	print('Hits w1: {}\nHits w2: {}'.format(prob1, prob2))
	print('Number of matches: ', prob12)
	print('PMI of {} and {}: {}'.format(word1, word2, pmi(prob1, prob2, prob12)))

def pmi(prob1, prob2, prob12):
	# calculates the pointwise mutual information
	return log(prob12/(prob1*prob2), 2)

def main():
	fileName = 'C:\\users\\mallison\\documents\\github\\playground\\THE MERCHANT OF VENICE.txt'
	with open(fileName) as f:
		text = f.read()
	around(text, 'Shylock', 'jew')
	around(text, 'Shylock', 'wealth')

	fileName = 'C:\\users\\mallison\\documents\\github\\playground\\magicians_nephew.txt'
	with open(fileName) as f:
		text = f.read()
	around(text, 'aunt', 'letty')
	around(text, 'uncle', 'andrew')
	
if __name__ == '__main__':
	main()