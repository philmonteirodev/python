lista = open("aula 06\listaCompras.txt", "w")
lista = open("aula 06\listaCompras.txt", "a")
print ("Digite S para adicionar um novo produto.")
pergunta = input ("Caso deseje imprimir a lista de compras, aperte qualquer outra tecla.")

while pergunta == "S" or pergunta == "s":
        produto = input()
        lista.write(produto + "\n")
        pergunta = input("Deseja adicionar um novo produto? S/N ")

lista.close()
lista = open("aula 06\listaCompras.txt", "r")
listafinal = lista.read()
print ("LISTA DE COMPRAS")
print(listafinal)