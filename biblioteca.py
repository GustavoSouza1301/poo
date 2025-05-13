from binascii import a2b_qp


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
    def __init__(self, numeroConta, nomeConta, tipoConta):
        self.nome = nomeConta
        self.numero = numeroConta
        self.tipoConta = tipoConta
        self.saldo = 0
        self.limite = 0
        self.status = False

    def ativarConta(self):
        if self.status == True:
            print("Conta já está ativa")
            print("-"*50)
        else:
            self.status = True
            print("Conta ativada")
            print("-"*50)

    def depositar(self,valor):
        if self.status == True:
            self.saldo += valor
            print("Deposito efetuado com sucesso.")
            print("-"*50)
        else:
            print("Conta não ativada")
            print("-"*50)

    def verificarSaldo(self):
        if self.status == True:
            print(f"Saldo: {self.saldo}")
            print("-"*50)
        else:
            print("Conta não ativada")
            print("-"*50)

    def sacar(self,valorSaque):
        if self.status == True:
            self.saldo -= valorSaque
            print(f"Saque efetuado com sucesso")
            print("-"*50)
        else:
            print("Conta não ativada")
            print("-"*50)

    def desativarConta(self):
        if self.saldo == 0 and self.status == True:
            self.status = False
            print("Conta desativada")
            print("-"*50)
        else:
            print("Conta não pode ser desativada")
            print("-"*50)

class Animal():
    def __init__(self,nome , cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer ...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"O {self.nome} foi miando... miauhh")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def latir(self):
        print(f"O {self.nome} tá latindo...")

class Vaca(Animal):
    def __init__(self, nome ,cor):
        super().__init__(nome,cor)

    def mugir(self):
        print(f"O {self.nome} está mugindo...")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def grunir(self):
        print(f"O {self.nome} está iiii iiii iiii...")

class Ingresso():
    def __init__(self,valor):
        self.valor = valor

    def imprimirValor(self):
        print(f"O valor do ingresso é {self.valor}")

class IngressoVip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
        self.valor *= 1.5

    def imprimirValor(self):
        print(f"O valor do ingresso VIP é {self.valor}")

class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calArea(self,base, altura):
        self.area = base * altura
        print(self.area)

    def calPerimetro(self, base , altura):
        self.perimetro = (base + altura) * 2
        print(self.perimetro)

class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calArea(self, base, altura,):
        self.area = (base * altura) / 2
        print(self.area)

    def calPerimetro(self, base, altura):
        self.perimetro = (base + altura)
        print(self.perimetro)

class Atleta:
    def __init__(self):
        self.aposentado = False
        self.peso = 0
        self.aquecer = False

    def aposentar(self):
        self.aposentado = True

    def aquecido(self):
        self.aquecer = True
        print("Acabou de aquecer")

class Corredor(Atleta):
    def __init__(self):
        super().__init__()

    def correr(self):
        if self.aquecer == True:
            print("Começou a correr")
        else:
            print("Precisa aquecer antes de correr")

class Nadador(Atleta):
    def __init__(self):
        super().__init__()

    def nadar(self):
        if self.aquecer == True:
            print("Começou a nadar")
        else:
            print("Precisa aquecer antes de nadar")

class Ciclita(Atleta):
    def __init__(self):
        super().__init__()
    def pedalar(self):
        if self.aquecer == True:
            print("Começou a pedalar")
        else:
            print("Precisa aquecer antes de pedalar")






