class Pessoa:
    def __init__(self,nome,peso,idade,falando=False,comendo=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo
        self.falando=falando
    def comer(self,comida):
        self.comida=comida
        if self.comendo==False:
            self.comida = comida
            self.comendo = True
            print(f'{self.nome} esta comendo {self.comida}')
        else:
            print(f'{self.nome} não pode comer pois já está comendo')
    def pararcomer(self):
        if self.comendo==True:
            self.comendo=False
            print(f'{self.nome} parou de comer')
        else:
            print("Não esta comendo!")

    def falar(self):
        if self.comendo==False:
            if self.falando==False:
                self.falando=True
                print(f'{self.nome} está falando')
        else:
            print(f'{self.nome} ele nao pode falar porque esta comendo')

    def parardefalar(self):
        if self.falando==True:
            self.falando=False
            print(f'{self.nome} parou de falar')

p1=Pessoa("joao",80,19)
p2=Pessoa("Maria",54,20)
p3=Pessoa("Bina",50,18)
print(f'{p1.nome} pesa {p1.peso} quilos e tem {p1.idade} anos')
print(f'{p2.nome} pesa {p2.peso} quilos e tem {p1.idade} anos')
print(f'{p3.nome} pesa {p3.peso} quilos e tem {p3.idade} anos')
p1.comer("feijão")
p1.comer("uva")
p1.falar()
p1.parardefalar()

p2.comer("feijão")
p2.comer("uva")
p2.falar()
p2.parardefalar()