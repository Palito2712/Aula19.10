lista = []
contador = 0
par = 0
impar = 0

while len(lista) < 10:
    numeros = int(input("Digite um número inteiro: "))
    lista.append(numeros)
    contador =+ 1

for numero in lista:
    if numero % 2 == 0:
        par += 1

    else:
        impar += 1

print("O maior número digitado foi: ", max(lista))
print("O menos número digitado foi: ", min(lista))
print("A quantidade de números impares foi: ", impar)
print("A quantidade de números pares foi: ", par)
