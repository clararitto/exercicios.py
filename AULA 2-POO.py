class ContaBancaria:
    def __init__(self,numero_conta,nome_cliente,tipo_conta):
        self.numero_conta=numero_conta
        self.saldo_conta=0
        self.status_conta=False
        self.nome_cliente=nome_cliente
        self.tipo_conta=tipo_conta
    def ativar(self):
        if self.status_conta == False:
            self.status_conta=True
            print(f' A conta de {self.nome_cliente} está ativada')
    def desativar(self):
        if self.saldo_conta==0:
            self.status_conta=False
            print(f'A conta de {self.nome_cliente} está desativada')
        else:
            print(f'sua conta só pode ser desativada se {self.saldo_conta==0}')
    def verificar(self):
        if self.status_conta==True:
            print(f'o seu saldo da conta de {self.nome_cliente} é R$:{self.saldo_conta}')
        else:
            print(f'{self.nome_cliente} sua conta está DESATIVADA')
    def depositar(self,dinheiro):
        self.saldo_conta+=dinheiro
        print(f'{self.nome_cliente} seu saldo atual é R$:{self.saldo_conta}')
    def sacar(self,dinheiro):
        if dinheiro<=self.saldo_conta:
            self.saldo_conta-=dinheiro
            print(f'{self.nome_cliente},você sacou R$:{dinheiro}')
        else:
            print(f'{self.nome_cliente} o seu saldo é menor que o valor do saque')
    def liberar_limite(self):

p1=ContaBancaria("123456", "Maria","corrente")
p1.liberar_limite()
p1.ativar()
p1.depositar(10)
p1.sacar(20)
p1.verificar()
p1.desativar()