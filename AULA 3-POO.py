class Animal():
    def __init__(self,nome,cor,comendo=False):
        self.nome=nome
        self.cor=cor
        self.comendo=comendo

    def comer(self):
        self.comida=comida
        if self.comendo!=False:
            print(f'O {self.nome} foi comer{self.comendo}')
        else:
            print(f'O {self.nome} Não está comendo nada')
class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def Miar(self):
        print(f'O {self.nome} foi miando...')
    def comer(self,tipo):
        print(f'O {self.nome} foi comer {tipo}')

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def Latir(Animal):
        print(f'O {self.nome} foi latindo...')
    def comer(self, tipo):
        print(f'O {self.nome} foi comer {tipo}')
class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def Pular(Animal):
        print(f'O {self.nome} foi pulando...')
     def comer(self, tipo):
        print(f'O {self.nome} foi comer {tipo}')
class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def Mugir(Animal):
        print(f'O {self.nome} foi mugindo...')
    def comer(self, tipo):
        print(f'O {self.nome} foi comer {tipo}')
p1=Cachorro("lise","caramelo","ração")
p1.latir()
p1.comer(ração)
c1=Gato("tapioca","branco e cinza","ração")
c1.miar()
u1=Coelho=("coeiu","preto","ração")
u1=

p1=Animal("Gato","branco","ração")
p1=Animal("Coelho","marrom","cenora")
p1=Animal("Vaca","marrom e branca","mato")







