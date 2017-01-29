# around.py
from nltk import word_tokenize
from math import log

def simple_search(document, input, matchCase=False):
	if matchCase == False:
		input1 = input1.lower()
		input2 = input2.lower()
		document = document.lower()
	tokens = word_tokenize(document)
	print('Number of words: ', len(tokens))
	hits = 0
	for i, j in enumerate(tokens):
		if j == input:
			hits += 1
	return hits


def around(document, input1, input2, range=20, matchCase=False):
	if matchCase == False:
		input1 = input1.lower()
		input2 = input2.lower()
		document = document.lower()
	tokens = word_tokenize(document)
	print('Number of words: ', len(tokens))
	idx1 = []
	idx2 = []
	for i, j in enumerate(tokens):
		if j == input1:
			idx1.append(i)
		if j == input2:
			idx2.append(i)
	hits1 = len(idx1)
	hits2 = len(idx2)

	hits12 = 0
	idx12 = []
	for w1 in idx1:
		for w2 in idx2:
			# if the words occur together within the set range, they co-occur
			if abs(w1-w2) <= range:
				hits12 +=1
				idx12.append((w1,w2))
	# hits12 /= len(tokens)**2
	results = [hits1, hits2, hits12, idx1, idx2, idx12]
	return results


def around_phrase(document, idxPhrase, target, range=20, matchCase=False):
	if matchCase == False:
		target = target.lower()
		document = document.lower()
	tokens = word_tokenize(document)
	idxTarget = []
	for i, j in enumerate(tokens):
		if j == target:
			idxTarget.append(i)
	hitsTargetd = len(idxTarget)
	
	hitsTarget = 0
	for t in idxTarget:
		print(t)
		for p in idxPhrase:
			print(p)
			# LOOK AT THIS BITCH YOU HAVE SOMETHING WEIRD GOING ON WITH THE COUNTING OF TARGET HITSgit
			if abs(t-p[0])<=range or abs(t-p[1])<=range:
				hitsTarget += 1
	return hitsTarget


def pmi(hits1, hits2, hits12):
	# Turney added 0.01 to the probability of each word/phrase to avoid div/0
	hits1 += 0.01
	hits2 += 0.01
	# calculates the pointwise mutual information
	print(hits12, '/', hits1, '*', hits2)
	return log(hits12/(hits1*hits2), 2)


def turney(hitsPhrasePos, hitsPhraseNeg, hitsPos, hitsNeg):
	return log(hitsPhrasePos*hitsNeg/(hitsPhraseNeg*hitsPos), 2)


def main():
	fileName = 'C:\\users\\mallison\\documents\\github\\playground\\test.txt'
	with open(fileName) as f:
		text = f.read()
	word1 = 'yes'
	word2 = 'no'
	results = around(text, word1, word2, range=2)
	print('Instances of {}: {}\nInstances of {}: {}'.format(
		word1, results[0], word2, results[1]))
	print('Instances of co-occurrence: ', results[2])
	print('PMI of {} and {}: {}'.format('yes', 'no', pmi(
		results[0], results[1], results[2])))

	# print(results[5])
	# print(results[5][0])
	# print(results[5][0][0])
	# if results[5][0][0] == 0:
	# 	print('yar')

	target1 = 'excellent'
	target2 = 'poor'
	hitsExcellent = around_phrase(text, results[5], target1, range=2)
	hitsPoor = around_phrase(text, results[5], target2, range=2)
	print('Hits {}: {}\nHits {}: {}'.format(target1, hitsExcellent, 
		target2, hitsPoor))

	# fileName = 'C:\\users\\mallison\\documents\\github\\playground\\THE MERCHANT OF VENICE.txt'
	# with open(fileName) as f:
	# 	text = f.read()
	# around(text, 'Shylock', 'jew')
	# around(text, 'Shylock', 'wealth')

	# fileName = 'C:\\users\\mallison\\documents\\github\\playground\\magicians_nephew.txt'
	# with open(fileName) as f:
	# 	text = f.read()
	# around(text, 'aunt', 'letty')
	# around(text, 'uncle', 'andrew')
	
if __name__ == '__main__':
	main()