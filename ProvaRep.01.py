mes = 5
ano = 2023

nome = str(input("Olá, bem vindo a autoescola PUC! Qual é o seu nome? "))
print("Certo", nome, "agora me diz uma coisa.")
anoAluno = int(input("Qual é o ano do seu nascimento? "))
mesAluno = int(input("Certo, agora por favor, digite o seu mês de nascimento: "))

if ano - anoAluno > 18:
    print("Você pode começar as aulas!")

elif ano - anoAluno <= 18 and mes >= mesAluno:
    print("Você pode começar as aulas!")

elif ano - anoAluno < 18:
    print("Você ainda não pode iniciar as aulas!")

elif ano - anoAluno == 18 and mes == mesAluno:
    print("Você pode começar as aulas!")

else:
    print("Você não pode começar as aulas!")