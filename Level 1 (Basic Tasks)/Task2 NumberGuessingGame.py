import random

def NumberGuessingGame():
    Org_Number = random.randint(1, 100)
    attempt = 0
    Max_Attemt = 8
    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100.")
    print(f"You have {Max_Attemt} attempts to guess it.\n")

    while (attempt < Max_Attemt):
        try:
            attempt += 1
            Guess = int(input(f"Attempt: {attempt}, Enter your guess: "))

            if ((Guess < 1) or (Guess > 100)):
                print("Please guess a number between 1 and 100 only!")
            elif (Guess == Org_Number):
                print(f"Congratulations! You guessed the number {Org_Number} in {attempt} attempts.")
            elif Guess < Org_Number:
                print("Number is Too LOW! Try Again.")
            else:
                print("Number is Too High! Try Again.")
            
        except ValueError:
            print("Invalid input! Please enter a number.")
        
    else:
        print(f"Sorry, you have used all {Max_Attemt} attempts. The number was {Org_Number}.")

NumberGuessingGame()