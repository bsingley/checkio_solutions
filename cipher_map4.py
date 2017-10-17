#!/usr/bin/env python
# title: cipher_map.py
# description: Solution for checkio problem. https://py.checkio.org/mission/cipher-map2/solve/
# author: bsingley
# python_version: 3


def recall_password(cipher_grille, ciphered_password):
    solution = ''

    size = len(ciphered_password)

    
    #create a dictionary for 'how to rotate coordinates'
    list_of_coordinates = zip(sorted(list(range(size)*size)),(list(range(size)*size)))
    should_rotate_to = zip((list(range(size)*size)),(sorted(list(range(size - 1,-1,-1)*size), reverse = True)))

    list_of_coordinates = [(0,0),(0,1),(0,2),(0,3),
                       (1,0),(1,1),(1,2),(1,3),
                       (2,0),(2,1),(2,2),(2,3),
                       (3,0),(3,1),(3,2),(3,3)] 

    should_rotate_to =    [(0,3),(1,3),(2,3),(3,3),
                       (0,2),(1,2),(2,2),(3,2),
                       (0,1),(1,1),(2,1),(3,1),
                       (0,0),(1,0),(2,0),(3,0)]

    rotate_to_this = {}

    for x, y in zip(list_of_coordinates,should_rotate_to):
        rotate_to_this[x] = y

    #create key for coordinate to password letter
    letter_dict = {}

    row_count = 0
    for row in ciphered_password:
        letter_count = 0
        for letter in row:
            letter_dict[(row_count,letter_count)] = letter
            letter_count += 1
        row_count +=1


    #walk through the password grilled and find out where the letters are supposed to be. 
    pass_string_list2 = list()
    pass_string_list3 = list()
    pass_string_list4 = list()

    row_count = 0
    for row in cipher_grille:
        char_count = 0
        for char in row:
            if char =='X':
                solution += letter_dict[(row_count,char_count)]

                # get the next list of coordinates to run through the letter dict
                pass_string_list2.append(rotate_to_this[(row_count,char_count)])
                pass_string_list3.append(rotate_to_this[rotate_to_this[(row_count,char_count)]])
                pass_string_list4.append(rotate_to_this[rotate_to_this[rotate_to_this[(row_count,char_count)]]])
            char_count += 1
        row_count += 1

    for coord in sorted(pass_string_list2):
        solution += letter_dict[coord]

    for coord in sorted(pass_string_list3):
        solution += letter_dict[coord]

    for coord in sorted(pass_string_list4):
        solution += letter_dict[coord]      

    return solution









if __name__ == '__main__':
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
