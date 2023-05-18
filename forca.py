import random

print(" °°°JOGUINHO DA FORCA°°° ")
print("------CIDADES DE PERNAMBUCO------")
palavras_secretas = ["Olinda", "recife", "Jaboatão", "Camaragibe", "Paulista"]
palavra_secreta = random.choice(palavras_secretas)
tentativas = 0
chances = 7
letras_q_ja_foram = []
estado_atual = ["_"] * len(palavra_secreta)
print(estado_atual)

print("{ Seu objetivo é acertar a palavra secreta }")
print("{ Você terá que tentar uma letra por vez }")
print("{ Se você acertar, a letra será colocada no estado atual da palavra para você visualizar e chegar mais perto do acerto }")
print("*** Caso você erre, você perderá uma chance. Você tem", chances, "tentativas ***")

while tentativas < chances and ''.join(estado_atual) != palavra_secreta:
    letra = input("\n\nDigite uma letra: ")
    while letra in letras_q_ja_foram:
        print("Você já digitou essa letra")
        letra = input("\nDigite uma letra: ")
    letras_q_ja_foram.append(letra)
    if letra in palavra_secreta:
        print("Parabéns, você acertou a letra :)")
        for i in range(len(palavra_secreta)):
            if letra == palavra_secreta[i]:
                estado_atual[i] = letra
        print("Esse é o estado atual:", estado_atual)

        sabe_palavra = input("Você sabe a palavra secreta? (S/N): ").upper()
        if sabe_palavra == "S":
            palavra_usuario = input("Digite a palavra secreta: ").lower()
            if palavra_usuario == palavra_secreta:
                print("Parabéns! Você acertou a palavra secreta!")
                break
            else:
                print("Que pena! Você errou a palavra secreta.")
                break

    else:
        print("Que pena, você errou a letra :(")
        tentativas += 1
        print("Você já fez", tentativas, "tentativas e ainda tem", chances - tentativas, "tentativas")
        print("Esse é o estado atual:", estado_atual)
        print("Letras que já foram tentadas: ", letras_q_ja_foram)

if tentativas == chances:
    print("\nVOCÊ PERDEU, ACABARAM AS SUAS TENTATIVAS")
    print("A palavra era:", palavra_secreta)
else:
    print("\nVOCÊ GANHOU, PARABÉNS")
    sabe_palavra = input("Você sabe a palavra secreta? (S/N): ").upper()
    if sabe_palavra == "S":
        palavra_usuario = input("Digite a palavra secreta: ").lower()
        if palavra_usuario == palavra_secreta:
            print("Parabéns! Você acertou a palavra secreta!")

        else:
            print("Que pena! Você errou a palavra secreta.")

    else:
        print("A palavra era:", palavra_secreta)