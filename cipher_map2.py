def recall_password(cipher_grille, ciphered_password):
	solution = ''
	current_grille = cipher_grille

	solution = mapWindows(cipher_grille, ciphered_password)
	numRotate = 0

	while numRotate <= 3:
		rotateGrille()

	return solution


def mapWindows (cipher_grille, ciphered_password):
	#map the grille to a list of tuples - repeatable
	solution = ''
	rowcount = 0
	for row, line in zip(cipher_grille, ciphered_password):
		icount = 0
		rowcount += 1
		for x,y in zip(row, line):
			icount +=1
			if x == 'X':
				print ('found an X at this spot: %s, %s' %(rowcount, icount))
				print ('here/s the letter at that spot: %s' %y)
				solution = solution + y
		print(solution)

def rotateGrille (cipher_grille):
	#take the cipher_grille and output a new one rotated 90 degrees to the right
	new_grille = ()
	rowcount = 0
	for row, in cipher_grille:
		icount = 0
		for x,y in zip(row, line):
			icount +=1
			if x == 'X':
		rowcount += 1


def whatEqualsWhat(i):
	if i == 0:
		k = 3
	elif i == 1: 
		k = 2
	elif i == 2:
		k = 1
	elif i == 3:
		k = 0

	return (k)



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
