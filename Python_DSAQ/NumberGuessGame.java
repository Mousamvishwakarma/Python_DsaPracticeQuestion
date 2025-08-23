
import java.util.Scanner;
import java.util.Random;

public class NumberGuessGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.print("Enter your max number: ");
        int maxNum = scanner.nextInt();
        int randomNum = random.nextInt(maxNum) + 1; 

        scanner.nextLine(); 
        System.out.print("Guess a number (or type 'quit' to exit): ");
        String guess = scanner.nextLine();

        while (true) {
            if (guess.equalsIgnoreCase("quit")) {
                System.out.println("User quit the game.");
                break;
            }

            int guessNum;
            try {
                guessNum = Integer.parseInt(guess);
            } catch (NumberFormatException e) {
                System.out.print("Invalid input. Please enter a number: ");
                guess = scanner.nextLine();
                continue;
            }
            
            if (guessNum == randomNum) {
                System.out.println("You are right! Congrats Sir");
                break;
            } else if (guessNum < randomNum) {
                System.out.print("Hint: Your guess is too small. Try again: ");
            } else {
                System.out.print("Hint: Your guess is too large. Try again: ");
            }

            guess = scanner.nextLine();
        }

        scanner.close();
    }
}
