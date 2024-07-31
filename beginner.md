# Guessing game

The goal of the project is to create a simple guessing game where the player must guess a random number between 1 and 100

- The game ends when the user guess the correct number

- If the number is less than the random number : The program prints `Too low` and then `Guess again : ` 
- If the number is greater than the random number : The program prints `Too high` and then `Guess again : ` 
- If the number is the correct one:  The program prints The program prints `Congratulations ! You guessed the number.`

## Step 1

Go to [https://www.programiz.com/python-programming/online-compiler/](https://www.programiz.com/python-programming/online-compiler/)

## Step 2

Copy and past the following code in the editor

```python
from random import randint

def main():
    number_to_guess = randint(___,___) # To be completed


    print(" Welcome to the game ! ".center(50, "="))

    guessed = int(input("Guess a number between 1 and 100 : "))

    while guessed ___ number_to_guess: # To be completed
        if guessed ___ number_to_guess: # Write the correct operator
            print("___") # To be completed
        else:
            print("___") # To be completed

        guessed = int(input("Guess again : "))

    print("___") # To be completed



if __name__ == "__main__":
    main()
```

## Step 3

Complete the code by changing the syboles `___` with the appropriate terms.

## Step 4

Run the code 

Congratulation if everything worked well


## Resources

### `randint`

Generate a random number

```python
randint(a,b) # Generate a random number between a and b both included

# Example
randint(1, 10) # Generate a rabdom number between 1 and 10 both included
 
```

### `input`

Get an useer input on the terminal

``` python
a = input("Please enter a number")
```