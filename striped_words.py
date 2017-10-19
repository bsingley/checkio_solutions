#!/usr/bin/env python
# title: striped_words.py
# description: Solution for checkio problem. https://py.checkio.org/mission/striped-words/solve/
# author: bsingley
# python_version: 2.7


#You should count the number of words (striped words) 
#where the vowels with consonants are alternating, 
#that is; words that you count cannot have two consecutive vowels or consonants. 
#The words consisting of a single letter are not striped -- do not count those. #
#Casing is not significant for this mission.

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
	print text
	upper_l = [word.upper() for word in text.split() if len(word) > 1]

	result = [[i for i in range(len(word)) if word[i] in VOWELS] for word in upper_l]
	print result
	#result = [[i for i in word if i in VOWELS] for word in upper_l]

	print result

	#all odds
	print [[all(num%2 == 1 for num in lst)] for lst in result if len(lst)>0] 
	#all evens
	print [[all(num%2 == 0 for num in lst)] for lst in result if len(lst)>0] 

	

	count = len(text.split())
	print count

	return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"