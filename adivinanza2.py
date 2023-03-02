import random

numberToGuess = random.randint(0,20)

won = False

maxGuess = 3
contUserGuess = 0

while contUserGuess < maxGuess and not won:
    userInput = int(input("Adivina el numero entre 0 y 20: "))
    if userInput == numberToGuess:
        print("Has ganado")
        won = True
    else:
        print("Respuesta incorrecta")
        contUserGuess = contUserGuess + 1
        print(f"Te quedan {maxGuess - contUserGuess} intentos")

    if contUserGuess == maxGuess:
        print(f"Has perdido, el numero a encontrar era {numberToGuess}")