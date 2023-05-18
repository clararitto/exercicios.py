secret_palavra=["P","A","T","O"]
let_descobertas=[]
print("\n*** jogo da forca ***\n")

for x in range(0,len(secret_palavra)):
    let_descobertas.append("-")

acertou = False

while acertou == False:
    letra=str(input("Digite a letra: "))

    for x in range(0,len(secret_palavra)):
        if letra== secret_palavra[x]:
            let_descobertas[x]=letra
        print(let_descobertas[x])
    acertou=True
    for y in range(0,len(let_descobertas)):
        if let_descobertas[y]=="-":
            acertou=False