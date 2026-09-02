# guessing a number 
hidden_number = 18
guess = int(input("Guess the hidden number: "))
if guess == hidden_number:
    print("Correct! You guessed the hidden number.")
elif guess > hidden_number:
    print("High")
else:
    print("Low")        
