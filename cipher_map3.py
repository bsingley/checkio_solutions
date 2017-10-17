def recall_password(cipher_grille, ciphered_password):
    solution = ''

    # create a dictionary of coordinates and password letters
    letters_dict = create_dict(ciphered_password)

    #figure out the coordinates rotate around
    list_of_coordinates = zip(sorted(list(range(4)*4)),(list(range(4)*4)))
    should_rotate_to = zip((list(range(4)*4)),(sorted(list(range(3,-1,-1)*4), reverse = True)))

    rotate_to_this = {}

    for x, y in zip(list_of_coordinates,should_rotate_to):
        rotate_to_this[x] = y

    # find the coordinates where the X's are 
    # add the letters from those coordinates to 'solution'
    rotate_count = 0
    rowcount = 0

    next_list_of_coords = list()
    
    for row in cipher_grille:

        icount = 0
        for x in row:
            if x == 'X':
                print (rowcount, icount)
                print letters_dict[(rowcount,icount)]
                solution += letters_dict[rowcount,icount]
                print 'this coord: ', rowcount,icount, 
                        'will now become ',rotate_to_this[(rowcount,icount)]
                next_list_of_coords.append(rotate_to_this[(rowcount,icount)])
                print next_list_of_coords


            icount +=1
        rowcount += 1
    print solution
    new_list_of_coords = list()
    for coord in next_list_of_coords:
        solution += letters_dict[coord]
        new_list_of_coords.append(rotate_to_this[coord])
        print solution
        print new_list_of_coords



    while rotate_count<3:

        rotate_count +=1

        # rotate the board to the right 3x



    return solution





def create_dict(ciphered_password):
    # create a dictionary of coordinates and password letters
    coordinates = zip(sorted(list(range(4)*4)),(list(range(4)*4)))

    helpful_string = ''
    for row in ciphered_password:
        for letter in row: 
            helpful_string += letter
            #print helpful_string

    letters_dict = {}
    for letter, coord in zip(helpful_string,coordinates):
        letters_dict[coord] = letter

    #print letters_dict

    return letters_dict



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
