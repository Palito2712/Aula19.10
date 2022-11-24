#Profe, eu só não consegui colocar o crítico. Do jeito que eu consegui fazer, não sei e também não achei
#um jeito de armazenar esse número para usar depois. Eu vi aqui que existe o getstate() e o setstate() porém
#não consegui fazer funcionar.
import random

print("Bem vindo! Que a luta, COMECE!!")

vida = 200
vidaInimigo = 200

while vida > 0 and vidaInimigo > 0:

    comando = int(input("Digite 1 para Atacar ou 2 para Curar: "))

    if comando == 1:
        print("Você atacou!")
        vidaInimigo = vidaInimigo - random.randrange(50, 100)
        print("A vida do inimigo ficou: ", vidaInimigo)

        if vidaInimigo <= 0:
            print("Parabéns, você venceu!!")
            break
    else:
        print("Você se curou!")
        vida = vida + random.randrange(30, 50)
        print("A sua vida ficou: ", vida)

    print("É a vez do inimigo!!")
    inimigo = random.randint(1, 2)

    if inimigo == 1:
        print("Ele te atacou!")
        vida = vida - random.randrange(50, 100)
        print("A sua vida ficou: ", vida)
        if vida <= 0:
            print("Você perdeu!!")
            break

    else:
        print("Ele se curou!!")
        vidaInimigo = vidaInimigo + random.randrange(30, 50)
        print("A vida dele ficou: ", vidaInimigo)