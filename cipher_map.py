
#!/usr/bin/env python
# title: cipher_map.py
# description: Solution for checkio problem. https://py.checkio.org/mission/cipher-map2/solve/
# author: bsingley
# python_version: 3


#use list of tuples to find letters in password, add to string - repeatable
#rotate the grille - repeatable (should be a ton of if statements)

def recall_password(cipher_grille, ciphered_password):
    mapWindows(cipher_grille)



    return ""

def mapWindows (cipher_grille, ciphered_password):
    #map the grille Xs to list of tuples - repeatable

    #a list of tuples (coordinates) of where in the 4x4 grid these windows fall
    windows = []
    rowcount = 0
    icount = 0
    for row in cipher_grille, ciphered_password:
        rowcount +=1
        for i in row:
            icount +=1
            if i == 'X':
                print ('found an X at this location: %s' %(rowcount,icount)



if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'