# You are given a text, which contains different english letters 
# and punctuation symbols. 
# You should find the most frequent letter in the text. 
# The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, 
# so for the purpose of your search, "A" == "a". 
# Make sure you do not count punctuation symbols, digits and whitespaces, 
# only letters.
# If you have two or more letters with the same frequency, 
# then return the letter which comes first in the latin alphabet. 
# For example -- "one" contains "o", "n", "e" only once for each, 
# thus we choose "e".



def checkio(text):

    #place holder for final count of letter
    high_count = 0
    high_letter = ''
    
    # split and alphabetize string
    letters = list(text.lower())
    letters.sort()
    
    #count letters, only higher count replaces high letter
    for letter in letters:
        if letter.isalpha():
            count = text.lower().count(letter)
            if count > high_count:
                high_count = count
                high_letter = letter
    
    return high_letter