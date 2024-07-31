from random import randint

def main():
    number_to_guess = randint(1, 100)


    print(" Bienvenu dans le jeu ! ".center(50, "="))

    guessed = int(input("Devinez un nombre entre 1 et 100 : "))

    while guessed != number_to_guess:
        if guessed < number_to_guess:
            print("Trop petit")
        else:
            print("Trop grand")

        guessed = int(input("Devinez à nouveau : "))

    print("Félicitaion ! Vous avez deviné le nombre.")


if __name__ == "__main__":
    main()

