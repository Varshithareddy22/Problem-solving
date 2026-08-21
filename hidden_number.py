hidden_number = 7

guess = int(input("Guess the hidden number: "))

if guess == hidden_number:
    print("Correct! You guessed the number.")

elif guess > hidden_number:
    print("Too high!")

else:
    print("Too low!")