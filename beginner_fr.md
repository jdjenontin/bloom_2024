# Guessing game

Le but du projet est de créer un simple jeu de devinette où le joueur doit deiner un nombre générer de façon aléatoire entre 1 et 100

- Le jeu s'arrête quand le joueur devine le nombre correct
- Si le nombre est plus petit que le nombre deviné est plus petit que le nombre aléatoire le programme écrit `Trop petit` puis `Devinez à nouveau : `
- Si le nombre est plus petit que le nombre deviné est plus élevé que le nombre aléatoire le programme écrit `Trop grand` puis `Devinez à nouveau : `
- Si le nombre deviné est correct, le programme écrit `Félicitaion ! Vous avez deviné le nombre.`

## Etape 1

Aller sur [https://www.programiz.com/python-programming/online-compiler/](https://www.programiz.com/python-programming/online-compiler/)

## Etape 2

Copier et coller le code suivant dans l'éditeur

```python
from random import randint

def main():
    number_to_guess = randint(___,___) # A compléter


    print(" Bienvenu dans le jeu ! ".center(50, "="))

    guessed = int(input("Devinez un nombre entre 1 et 100 : "))

    while guessed ___ number_to_guess: # A completer
        if guessed ___ number_to_guess: # A completer
            print("___") # A completer
        else:
            print("___") # A completer

        guessed = int(input("Devinez à nouveau : "))

    print("___") # A completer



if __name__ == "__main__":
    main()
```

## Step 3

Completer le code en changeant les symboles `___` par les termes appropriés

## Step 4

Lancer le programme 

Félicitations si tout marche bien.


## Ressources

### `randint`

Genère un nombre aléatoir

```python
randint(a,b) # Génère un nombre aléatoire entre a et b, les deux inclus

# Example
randint(1, 10) # Génère un nombre aléatoire entre 1 et 10, les deux inclus
 
```

### `input`

Prend une entrée de l'utilisateur sur le terminal

``` python
a = input("Entez un nombre svp")
```