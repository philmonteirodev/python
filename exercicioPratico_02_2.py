import random

def aleatorio ():
    return random.randint(1,100)

def avaliar (guess, numero):
        
        if guess < 1 or guess > 100:
             return "invalido"
        
        elif guess > numero:
            return "menor"
        
        elif guess < numero: 
            return "maior"
        
        else:
            return "correto"

numero = aleatorio()

while True:

        guess = int(input("Tente adivinhar o número de 1 a 100 que eu escolhi: "))
        resultado = avaliar(guess,numero)
    
        if resultado == "correto":
            print(f"Acertou!! O número escolhido é {numero}!!")
            break
        
        if resultado == "invalido":
            print("O número digitado é inválido. Digite um número de 1 a 100. ")
        else:
            print(f"O numero é {resultado}. Tente novamente.")

    
        

         




