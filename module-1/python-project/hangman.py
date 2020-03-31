import random

#Game header
print('')
print ('******H A N G M A N**********')
print('--------')
print('| 	|')
print('| 	')
print('| ')
print('| ')
print('| ')
print('|')
print('|')
print('---')

#welcome
print('Enter your name:')
name=input()
print('')
print("Welcome",name,"!","Save the prisoner by guessing the password before it's too late")
print('')

#variables
words={'anaconda': 'animal','hedgehog':'animal','kangaroo':'animal','banana':'fruit','mango':'fruit','guava':'fruit'}
word=random.choice(list(words))
user_word='' #accumulates the letters that the user enters
lifes_left=5
answer='y' 

while answer=='y':
	while lifes_left>0:   #the game will loop this while there are lifes left. 

		print('')
		mistakes=0
		for l in word:
			if l in user_word:
				print(l,end='') #accumulates correct letters and leaves underscores for remaining letters.
			else:
				print('  _',end='') #prints underscores depending on the number of letters of the word.
				mistakes+=1 
		if mistakes==0:   
			print('You saved the prisoner')
			answer=input('Play again? y/n : ')
			break

		print('')	
		print('')

		print('','the password is made of:',len(word),'letters')
		print('', 'hint:',words[word])	#game will continuously show the hint deppending on the word's value.

#this loop will prevent user from entering anything other than one letter and will count the letter only when conditions are satisfied.
		while True:
			letter=input('Introduce una letra: ').lower()
			if len(letter) !=1:
				print('Enter just one letter')
			elif letter in user_word:
				print('You already entered that letter')
			elif not letter.isalpha():
				print('Not a valid character')
			else:	
				user_word+=letter
				break

#finally if the letter that the user enters is not in the word, this conditional will decrease lifes by 1.
		if letter not in word:
			lifes_left-=1
			print('')
			print('**Letter', letter,'is not part of the password**')
			print('			Attempts left=',lifes_left)

#whenever lifes are over, game will display the following.
		if lifes_left == 0:
			print('the password was: ',word)

	else:
		print('******you lose*******')
		print('------')
		print('|    O')
		print('|   /|\ ')
		print('|  / | \ ')
		print('|    |  ')
		print('|   / \ ')
		print('|')
		print('|')
		print('')
		answer=input('Play again? y/n : ')