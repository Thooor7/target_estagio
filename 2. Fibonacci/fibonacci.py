numero = int(input("Digite um número: "))

fibonacci = [0, 1]

while fibonacci[-1] < numero:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])


if numero in fibonacci:
      print(numero, "pertence à sequência de Fibonacci: ", fibonacci)
else: 
    print(numero, "não pertence à sequencia de Fibonacci!")