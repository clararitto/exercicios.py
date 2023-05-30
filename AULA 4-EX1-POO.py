class Atleta:
    def __init__(self,peso,nome):
        self.peso=peso
        self.nome=nome
        self.aposentado=False
        self.aquecendo=False

    def Aposentar(self):
        if self.aposentado==False:
            self.aposentado=True
    def Aquecer(self):
        if self.aquecendo==False:
            self.aquecendo=True

class Nadador(Atleta):

    def __init__(self,peso):
        super().__init__(peso)
    def nadar(self):
        if self.aposentado==False:
            if self.aquecendo==True:
                print(f'O {self.nome} está nadando')
        else:
            print(f'O nadador {self.nome} precisa está {self.aquecendo}')
            else:
                print(f' O atleta {self.nome} não pode nadar,poque já está fazendo outra atividade')
class Ciclista(Atleta):

    def pedalar(self):
         if self.aposentado==False:
            if self.aquecendo==True:
                print(f'O {self.nome} está pedalando')
        else:
            print(f'O ciclista {self.nome} precisa está {self.aquecendo}')
            else:
                print(f' O atleta {self.nome} não pode pedalar,poque já está fazendo outra atividade')
class Corredor(Atleta):

    def correr(self):
         if self.aposentado==False:
            if self.aquecendo==True:
                print(f'O {self.nome} está correndo')
        else:
            print(f'O corretor {self.nome} precisa está {self.aquecendo}')
            else:
                print(f' O atleta {self.nome} não pode correr,poque já está fazendo outra atividade')
class TriAtleta(Nadador,Ciclista,):
    def __init__(self,peso):
        super().__init__(peso)
    def correr(self):
        if self.aposentado==False:
            if self.aquecendo==True:
                if self.nadando==False:
                    if self.pedalando==False:
                        if self.correndo==True:
                            print(f'O corredor {self.nome} está correndo')
                    else:
                        print(f'o corredor não pode correr pois está pedalando')
                else:
                    print(f'O atleta não  pode correr pois está nadando')
            else:
                print(f'O corredor precisa se aquecer antes de se exercitar')
        else:
            print(f'O atleta{self.nome} não pode fazer exercicio porque está aposentado')
    def pedalar(self):
        if self.aposentado==False:
            if self.aquecendo==True:
                if self.nadando==False:
                    if self.correndo==False:
                        if self.pedalando==True:
                            print(f'{self.nome} ciclista está pedalando ')
                        else:
                            
