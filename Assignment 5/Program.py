import random



def hilo(guess, answer):
	
	if(guess < answer):
		print("Your guess is too low, try again")
		guess = int(input("Please enter your guess"))
	elif(guess > answer):
		print("Your guess is too high, please try again.")
		guess = int(input("Please enter your guess"))
	else:
		print("Congratulations you are not the suck. You're prize is an inflated ego.")
		return
	
	hilo(guess, answer)


answer = random.randint(1,20)
#This is the first guess, starting the game.
guess = int(input("Hi this is a hilo game. Please enter a number betweewn 1 and 20 and see if you can guess the correct number! Don't forget to have fun. Please enter your first guess."))


hilo(guess, answer)
