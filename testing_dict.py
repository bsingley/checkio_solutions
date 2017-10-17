ciphered_password = ('itdf',
         'gdce',
         'aton',
         'qrdi')



#figure out dictionary to swap the coordinates in the cipher map

list_of_coordinates = [(0,0),(0,1),(0,2),(0,3),
                       (1,0),(1,1),(1,2),(1,3),
                       (2,0),(2,1),(2,2),(2,3),
                       (3,0),(3,1),(3,2),(3,3)] 

should_rotate_to =    [(0,3),(1,3),(2,3),(3,3),
                       (0,2),(1,2),(2,2),(3,2),
                       (0,1),(1,1),(2,1),(3,1),
                       (0,0),(1,0),(2,0),(3,0)]


print list_of_coordinates == zip(sorted(list(range(4)*4)),(list(range(4)*4)))
print should_rotate_to == zip((list(range(4)*4)),(sorted(list(range(3,-1,-1)*4), reverse = True)))

rotate_to_this = {}

for x, y in zip(list_of_coordinates,should_rotate_to):
	rotate_to_this[x] = y

#print rotate_to_this



#sort a list of coordinates

unsorted = [(0,0),(0,3),(3,1),(2,2),(1,2)]
print unsorted

print sorted(unsorted)