peso = float(input("Olá! Para sabermos o seu IMC, por favor, digite o seu peso: "))
altura = float(input("Cerot, agora digite a sua altura: "))

imc = peso / altura**2

magrezaGrave = imc < 16
magrezaModerada = 16 < imc < 17
magrezaLeve = 17 < imc < 18.5
saudavel = 18.5 < imc < 25
sobrepeso = 25 < imc < 30
obesidadeGrau1 = 30 < imc < 35
obesidadeGrau2 = 35 < imc < 40
obesidadeGrau3 = imc >= 40

if imc < 16:
    print("Você está com magreza GRAVE!")

elif 16 < imc < 17:
    print("Você está com magreza moderada!")

elif 17 < imc < 18.5:
    print("Você está com magreza leve!")

elif 18.5 < imc < 25:
    print("Você está SAUDÁVEL!")

elif 25 < imc < 30:
    print("Você está com sobrepeso!")

elif 30 < imc < 35:
    print("Você está com obesidade de grau 1!")

elif 35 < imc < 40:
    print("Você está com obesidade de grau 2!")

elif imc >= 40:
    print("Você está com obesidade de grau 3!")