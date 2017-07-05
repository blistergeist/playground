# around.py
from nltk import word_tokenize, bigrams, pos_tag, ngrams
from nltk.corpus import stopwords
from math import log
import numpy as np

def word_search(tokens, word):
    hits = 0
    idx = []
    for i, j in enumerate(tokens):
        if j == word:
            hits += 1
            idx.append(i)
    return hits, idx


def bigram_extractor(tokens):
    stopWords = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stopWords]

    posTokens = pos_tag(tokens)
    trigrams = list(ngrams(posTokens, 3))
    hits = 0
    # print(trigrams)
    bigrams = []
    for t1, t2, t3 in trigrams:
        pos = [t1[1], t2[1], t3[1]]
        print(pos)
        if pos[0] == 'JJ' and pos[1][:2] == 'NN':
            hits += 1
            bigrams.append((t1[0], t2[0]))
        if pos[0][:2] == 'RB' and pos[1] == 'JJ' and pos[2][:2] != 'NN':
            hits += 1
            bigrams.append((t1[0], t2[0]))
        if pos[0] == 'JJ' and pos[1] == 'JJ' and pos[2][:2] != 'NN':
            hits += 1
            bigrams.append((t1[0], t2[0]))
        if pos[0][:2] == 'NN' and pos[1] == 'JJ' and pos[2][:2] != 'NN':
            hits += 1
            bigrams.append((t1[0], t2[0]))
        if pos[0][:2] == 'RB' and pos[1][:2] == 'VB':
            hits +=1
            bigrams.append((t1[0], t2[0]))
    print('Hits: ', hits)
    # savedBigrams = [(first[0], second[0]) for first, second in bigrams]
    # print(savedBigrams)
    # print(bigrams)
    return bigrams


def bigram_search(tokens, bigram=['lucky','stars']): 
    bigram = tuple(bigram)
    hits = 0
    idx = []
    for i, b in enumerate(bigrams(tokens)):
        if b == bigram:
            hits += 1
            idx.append(i)
    return hits, idx


def around(tokens, input1, input2, range=20):
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
                idx12.append([w1,w2])
    results = [hits1, hits2, hits12, idx1, idx2, idx12]
    return results


def around_bigram(tokens, bigram, target, range=10, matchCase=False):
    bigramHits, bigramIdx = bigram_search(tokens, bigram)
    targetHits, targetIdx = word_search(tokens, target)
    # print('Bigram hits: {}'.format(bigramHits))
    # print('Bigram indices: {}'.format(bigramIdx))
    # print('Target hits: {}'.format(targetHits))
    # print('Target indices: {}'.format(targetIdx))

    aroundHits = 0
    for b in bigramIdx:
        for t in targetIdx:
            if abs(b-t) <= range:
                aroundHits += 1
                break
    # print('Hits of "{0[0]} {0[1]}" near "{1}": {2}'.format(
    #     bigram, target, aroundHits))
    # print('Hits of {}: {}'.format(target, targetHits))
    return aroundHits, targetHits


def pmi(hits1, hits2, hits12):
    # Turney added 0.01 to the probability of each word/phrase to avoid div/0
    hits1 += 0.01
    hits2 += 0.01
    hits12 += 0.01
    # calculates the pointwise mutual information
    print(hits12, '/', hits1, '*', hits2)
    return log(hits12/(hits1*hits2))


def turney(posPhraseHits, negPhraseHits, posHits, negHits):
    posPhraseHits += 0.01
    negPhraseHits += 0.01
    posHits += 0.01
    negHits += 0.01
    if posPhraseHits < 2 and negPhraseHits < 2:
        return 0
    else:
        return log((posPhraseHits*negHits)/(negPhraseHits*posHits))
    # something is going on here. If there is a single instance of the
    # phrase near a negative target, the score goes to shit.


def main():
    fileName = 'test.txt'
    with open(fileName) as f:
        text = f.read()
    tokens = word_tokenize(text)
    word1 = 'always'
    word2 = 'happy'
    # results = around(text, word1, word2, range=2)
    # print('Instances of {}: {}\nInstances of {}: {}'.format(
    #   word1, results[0], word2, results[1]))
    # print('Instances of co-occurrence: ', results[2])
    # print('PMI of {} and {}: {}'.format('yes', 'no', pmi(
    #   results[0], results[1], results[2])))

    badWords = ['loss', 'horror', 'disappointing', 'cutting', 'delay', 'failure', 'distress', 'soft', 'abysmal',
                'bankruptcy']
    bigram = [word1, word2]
    posTarget = 'loss'
    negTarget = 'poor'
    posPhraseHits, posHits = around_bigram(tokens, bigram, posTarget, range=10)
    negPhraseHits, negHits = around_bigram(tokens, bigram, negTarget, range=10)
    score = turney(posPhraseHits, negPhraseHits, posHits, negHits)
    print('Turney algorithm score: {}\n'.format(score))

    bigrams = bigram_extractor(tokens)
    cumScore = []
    for b in set(bigrams):
        posPhraseHits, posHits = around_bigram(tokens, b, posTarget, range=10)
        negPhraseHits, negHits = around_bigram(tokens, b, negTarget, range=5)
        score = turney(posPhraseHits, negPhraseHits, posHits, negHits)
        print('Bigram: ', b)
        print('Turney algorithm score: {}\n'.format(score))
        cumScore.append(score)
    print('Average score: {}'.format(np.mean(cumScore)))



    # target1 = 'excellent'
    # target2 = 'poor'
    # hitsExcellent = around_phrase(text, results[5], target1, range=2)
    # hitsPoor = around_phrase(text, results[5], target2, range=2)
    # print('Hits {}: {}\nHits {}: {}'.format(target1, hitsExcellent, 
    #   target2, hitsPoor))

    # fileName = 'C:\\users\\mallison\\documents\\github\\playground\\THE MERCHANT OF VENICE.txt'
    # with open(fileName) as f:
    #   text = f.read()
    # around(text, 'Shylock', 'jew')
    # around(text, 'Shylock', 'wealth')

    # fileName = 'C:\\users\\mallison\\documents\\github\\playground\\magicians_nephew.txt'
    # with open(fileName) as f:
    #   text = f.read()
    # around(text, 'aunt', 'letty')
    # around(text, 'uncle', 'andrew')
    
if __name__ == '__main__':
    main()
