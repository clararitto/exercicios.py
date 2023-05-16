def somar(x,y):
    soma =0
    soma =x+y
    return soma
def subtrair(x,y):
    sub =0
    sub =x-y
    return sub
def multiplicar(x,y):
    multi =0
    multi =x*y
    return multi
def dividir(x,y):
    div =0
    div =x/y
    return div



def imprime_nome(nome):
    print(f"Nome:{nome}")


def exercicio(a):
    for i in range(1,a):
        for j in range(1,i+1):
            print(j,end=" ")
        print()


def cont_vogais(t):
    vogais="aeiou"
    cont=0
    for x in t:
        if x in vogais:
            cont+=1
    return print(cont)


def letras(t):
    cont=0
    for x in t:
        if x !=" ":
            cont+=1
    print(cont)

def estoque(produto_t,quantidade_q,valor_v):
    valor=quantidade_q*valor_v
    return valor, produto_t

def numero(a):
    if num!=0:
        if num >0:
            return "P"
        else:
            return "N"
    else:
        return "Z"
def somar_numeros(*numeros):
    soma=0
    for a in numeros:
        soma +=a
    return soma

def lista(a):
    lista2=[]
    for x in a:
        if x not in lista2:
            lista2.append(x)
    return list

def num_primo(a):
   calculo=a%a==1 and a%1==1

    if a==calculo:
        return("numero primo")
    else:
        return("não é primo")
