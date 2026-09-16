# guessing a hidden no number 
hidden_number = 18
guess = int(input("Guess a the hidden number: "))
if guess == hidden_number:
    print("Correct! You guessed correctly the hidden number.")
elif guess > hidden_number:
    print("High")            
else:
    print("Low")             
