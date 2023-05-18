import random
print(" °°°JOGUINHO DA FORCA°°° ")

palavras_secret=["gato","recife","pato","mesa","rato","cachorro"]
palavras_secret=random.choice(palavras_secret)
tentativas=0
chances=2
letras_q_ja_foram=[]
estado_atual=["_"]*len(palavras_secret)
print(estado_atual)
print("{ Seu objetivo é acertar a palavra secreta }")
print("{ Você terá que tentar uma letra por vez }")
print("{ Se você acertar,a letra vai ser colocada no estado atual da palavra para você vizualizar e chegar mais perto do acerto} ")
print("*** Caso você erre,você perderá uma chance,você tem" ,chances,"tentativas ***")
while tentativas<chances and ''.join(estado_atual)!= palavras_secret:

    letra=input("\n\nDigite uma letra: ").lower()
    while letra in letras_q_ja_foram:
        print("Você já digitou essa letra")
        letra = input("\nDigite uma letra: ").lower()
    letras_q_ja_foram.append(letra)
    if letra in palavras_secret:
        print("Parabéns,Você acertou a letra :)")
        for i in range(len(palavras_secret)):
            if letra==palavras_secret[i]:
                estado_atual[i]=letra
                print("Esse é o estado atual:", estado_atual)

    else:
        print("Que pena,Você errou a letra :(")
        tentativas+=1




        #quantas tentativas ele tem
        print("Você já fez",tentativas,"tentativas e ainda tem",chances-tentativas,"tentativas")
        #qual o estado atual da palavra
        print("Esse é o estado atual:",estado_atual)
        #quais as letras ele ja tentou
        for item in letras_q_ja_foram:
            print(item,end=" ")
        # fazer um final
if tentativas==chances:
    print("\nVOCÊ PERDEU,ACABARAM AS SUAS TENTATIVAS")
else:
    print("\nVOCÊ GANHOU,PARABÉNS")
print("A palavra era:",palavras_secret)
