#AI program that seeks to guess words from a dictionary based on the dictionary's3 grammar
#Walter Verburg - 8/28/2016 - present
#imports
import random
import sys

#load the dictionary file into a simple set
def getDic():
    fdic = open(sys.argv[1])
    dic = set()
    for word in fdic:
        dic.add(word.lower())
    return dic

# counts out and assigns weights to letters in a 2D dictionary
# first dimension is the preceding letter
# first content/second dimension is the succeeding letter
# second content is the probablistic weight of that letter
def getWeights(words):
	alphabet = "^abcdefghijklmnopqrstuvwxyz\n" #newline signifies end of word, "^" is the beginning
	weights = dict()
	for i in alphabet:
		subDic = dict()
		weights[i] = subDic
		subDic['total'] = 0
		for l in alphabet:
			subDic[l] = 0
	#add words to weights
	for word in words:
		#print(word)
		if (False): #len(word) < 3):
			print(word[:-1], "is too short")
		else:
			weights['^'][word[0]] += 1
			weights['^']['total'] += 1
			for i in range(len(word)-1):
				letterFrom = word[i]
				letterTo   = word[i+1]
				#print(letterFrom, '->', letterTo)
				weights[letterFrom][letterTo] += 1
				weights[letterFrom]['total'] += 1
	
	return weights

# picks a value from a given 1D dictionary based on weights within the dictionary
# in the context, dic is the characters that can follow a previous character
# there is no need to know the previous character here
def weightedPick(dic):
	#print("TOTAL DIC", dic['total'])
	rand = random.randrange(dic['total'])
	for option in dic:
		if option is 'total':
			continue
		#print(option, dic[option])
		rand -= dic[option]
		if (rand <= 0):
			return option
	print("Something went wrong with weightedPick, returned 'e'")
	return "e"

# just keep guessing
def guess(words, weights):
	count = 0
	stillTrying = True
	while (stillTrying):
		count += 1
		curr = weightedPick(weights['^'])
		word = ""
		while (curr != '\n'):
			word += curr
			#print("String:["+string+"]")
			#print("Curr:["+curr+"]")
			curr = weightedPick(weights[curr])
		#test for success
		if (len(word) > 3 and word+"\n" in words):
			stillTrying = False
			print(word, "is a word!")
			print("and it only took", count, "tries!")
		else:
			print("Nope:", word)

#main
words = getDic()
weights = getWeights(words)
#print(weights)
guess(words, weights)
