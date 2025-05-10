class Pessoa():
    def __init__(self, nome, idade, peso): # __init__ metodo construtor ou especial
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.falando = False
        self.comendo = False
        self.dormindo = False

    def falar(self):
        if self.comendo == True:
            print(f"{self.nome} não pode falar enquanto come.")
            print("-"*60)
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar enquanto dorme")
            print("-" * 60)
        elif self.falando == True:
            print(f"{self.nome} já está falando")
            print("-" * 60)
        else:
            self.falando = True
            print(f"{self.nome} começou a falar")
            print("-" * 60)

    def pararFalar(self):
        if self.falando == True:
            self.falando = False
            print(f"{self.nome} parou de Falar")
            print("-" * 60)
        else:
            print(f"{self.nome} não está falando")
            print("-" * 60)

    def comer(self):
        if self.falando == True:
            print(f"{self.nome} não pode comer enquanto fala")
            print("-" * 60)
        elif self.dormindo == True:
            print(f"{self.nome} não pode comer enquanto dorme")
            print("-" * 60)
        elif self.comendo == True:
            print(f"{self.nome} já está comendo")
            print("-" * 60)
        else:
            self.comendo = True
            print(f"{self.nome} começou a comer")
            print("-" * 60)

    def pararComer(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} parou de comer")
            print("-" * 60)
        else:
            print(f"{self.nome} não está comendo")
            print("-" * 60)

    def dormir(self):
        if self.comendo == True:
            print(f"O {self.nome} não pode dormir pq tá comendo")
            print("-" * 60)
        elif self.falando == True:
            print(f"O {self.nome} não pode dormir pq está falando")
            print("-" * 60)
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo")
            print("-" * 60)
        else:
            self.dormindo = True
            print(f"O {self.nome} dormiu")
            print("-" * 60)

    def acordar(self):
        if self.dormindo == True:
            self.dormindo = False
            print(f"{self.nome} miseravi acordou")
            print("-" * 60)
        else:
            print("Ele já está acordado")
            print("-" * 60)

class ContaBancaria:
    def __init__(self, numero, nome, tipoConta):
        self.nome = nome
        self.numero = numero
        self.tipoConta = tipoConta
        self.saldo = 0
        self.status = False
        self.limite = 0

    def ativaConta(self):
        if self.status:
            print("Conta já está ativada")
        else:
            self.status = True
            print("Conta  ativa")

    def depositar(self,valor):
        if self.status == True:
            self.saldo += valor
        else:
            print("Conta não ativada")

    def verificarSaldo(self):
        if self.status == True:
            print(self.saldo)
        else:
            print("Conta não ativada")

    def sacar(self,valorSaque):
        if self.status:
            self.saldo -= valorSaque
            print(f"Saque efetuado com sucesso")
        else:
            print("Conta não ativada")

    def desativarConta(self):
        if self.saldo == 0:
            self.status = False
            print("Conta desativada")
        else:
            print("Conta não pode ser desativada")

