import random
def number_guessing_game():
    print("welcome to the Number guesssing game")
    print("I have chosen a number between 1 and 100")
    print("Can you guess it?")
    
    secret_number = random.randint(1,100)
    attempt = 0
    
    while True:
        try:
            guess = int(input("Enter your guess:"))
            attempt +=1
            
            if guess == secret_number:
                print("congo;you guessed right number")
                break
            elif guess < secret_number:
                print("too low! try again")
            else:
                print("Too high!try again")
            
        except ValueError:
            
            print("please enter a valid integer")
         
number_guessing_game()   