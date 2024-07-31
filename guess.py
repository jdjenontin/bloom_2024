from random import randint

def main():
    number_to_guess = randint(1, 100)


    print(" Welcome to the game ! ".center(50, "="))

    guessed = int(input("Guess a number between 1 and 100 : "))

    while guessed != number_to_guess:
        if guessed < number_to_guess:
            print("Too low")
        else:
            print("Too high")

        guessed = int(input("Guess again : "))

    print("Congratulations ! You guessed the number.")


if __name__ == "__main__":
    main()

