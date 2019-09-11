import turtle,math

def Fer (F):
	c=((F-32)*(5/9))
	print("Your number converted to celcius is "+str(c)+" celcius")


def Acre (A):
	barnes=(A*4.047e+31)
	print("Your number converted to barnes is "+str(barnes)+" barnes")

userInput=int(input("What do you want to change from fahrenheit to celcius?"))

Fer (userInput)

userInput=int(input("What do you want to change from acres to barnes?"))

Acre (userInput)

def Shape (S):
	jon=turtle.Turtle()
	counter = 1
	while(S >= counter):
		jon.forward(50)
		jon.left(360/S)
		counter = 1 + counter
	screen=turtle.getscreen()
	screen.mainloop()
		
	
	

turInput=int(input("Please enter the number of sides that you want, but please make greater than 2, but don't make it too big or you gonna be here for a while"))

Shape (turInput)
