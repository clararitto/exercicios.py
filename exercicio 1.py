"""def somar(x,y):
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
menu=1
while menu>0 and menu<6:
    menu = int(input("1:SOMAR,2:SUBTRAIR,3:MULTIPLICAR,4:DIVIDIR,5:SAIR"))
    if menu==5
        break
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite outro numero: "))
    if menu==1:
        print(somar(n1,n2))
    elif menu==2:
        print(subtrair(n1,n2))
    elif menu==3:
        print(multiplicar(n1,n2))
    elif menu==4:
        print(dividir(n1,n2))
    elif menu==5:
        break
"""
"""def imprime_nome(nome):
    print(f"Nome:{nome}")
imprime_nome("Erickson")
imprime_nome("Renan")
imprime_nome("Daniel")"""

def exercicio(a):
    for i in range(1,a):
        for j in range(1,i+1):
            print(j,end=" ")
        print()


exercicio(6)