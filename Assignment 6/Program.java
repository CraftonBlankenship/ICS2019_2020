import java.util.Scanner;

public class Program{
	public static void main(String args[]){
	
	//The user input
	Scanner input = new Scanner(System.in);
	System.out.println("Please enter a number of sides you'd like me to draw.");
	int	sides = input.nextInt();
	
	
	
	//The inner angle of the polygon per side
	int angle = 360 / sides;
	int counter = sides;
	//Created turtle here 
	Turtle jesus;
	jesus = new Turtle();
	
	
	polygon(angle, counter, sides, jesus);
	
	
	
	
		}
	
	
	//method that reruns the program until proper number of sides have been drawn.
	
public static void polygon(int angle, int counter, int sides, Turtle jesus){

	if(counter > 0){
		jesus.forward(50);
		jesus.left(angle);
		counter = counter - 1;
	
			}
		polygon(angle, counter, sides, jesus);
}
}
