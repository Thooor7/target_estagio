nome = input("Escreve uma palavra para ser invertida: ")
invertido = ""

for i in range(len(nome)-1, -1, -1):
    invertido += nome[i]

print(f"A palavra {nome} invertida é {invertido.capitalize()}")