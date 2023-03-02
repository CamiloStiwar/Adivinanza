import random

maxGuess = 3
contUserGuess = 0



def buildListOfRandomNumbers(n):
    listOfRandomNumbers = []
    for randomNumber in range(0,n):
        listOfRandomNumbers.append(random.randint(0,20))
    return listOfRandomNumbers


def findNumber(numberToFind, listToSearch):
    
    if numberToFind in listToSearch:
        return print("El numero si se encuentra")
    return print("El numero no se encuentra")


numeroUsuario = int(input("Digite el número que desea adivinar: "))
randomList = buildListOfRandomNumbers(20)
encontrar = findNumber(numeroUsuario, randomList)
print(randomList)














#hacer un juego de piedra papel o tijera, el computador elige aleatoriamente piedra papel y tijera y debe pedir al usuario su input, el juego debe terminar cuando alguno de los
#dos gane 2 de 3 partidas