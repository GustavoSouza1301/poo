class Pessoa():
    def __init__(self, nome, idade, peso): # __init__ metodo construtor ou especial
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.falando = False
        self.comendo = False
        self.dormindo = False

    def dormir(self):
        if self.dormindo  == True:
            print(f"{self.nome} já está dormindo")
        elif self.falando == True:
            print(f"O {self.nome} não pode dormir pq tá falando")
        elif self.comendo == True:
            print(f"O {self.nome} não pode dormir pq tá comendo")
        else:
            print(f"O {self.nome} dormiu")
            self.dormindo == True

    def acordar(self):
        if self.dormindo == True:
            self.dormindo == False
            print("Acordou o miseravi")
        else:
            print("Ele já está acordado")

class ContaBancaria:
    def __init__(self, numero, nome, tipoConta):
        self.nome = nome
        self.numero = numero
        self.tipoConta = tipoConta
        self.saldo = 0
        self.status = False
        self.limite = 0

    def depositar(self,deposito):
        if self.status == True:
            self.saldo += deposito
        else:
            print("Conta não ativada")

    def verificarSaldo(self):
        print(self.saldo)

    def sacar(self,valorSaque):
        self.saldo -= valorSaque
        print(f"Saque efetuado com sucesso")

    def ativaConta(self):
        if self.status == False:
            self.status = True
            print("Conta ativada")
        else:
            print("Conta já está ativa")

    def desativarConta(self):
        if self.saldo == 0
            self.status = False
            print("Conta desativada")
        else:
            print("Conta não ser desativada")












"""A programação orientada a objetos possui 4 pilares:
Abstração; (Abstrair a complexidade que está por trás de algo)
Encapsulamento; (Ligado a proteção)
Herança; (Quando uma classe herda caracteristicas de outra)Super Classe\Classe Mãe\Classe Pai
Mensagem: Comunicação entre objetos através de apis.
Polimorfismo. É quando se pega métodos já existentes e .
Exemplo:
Polimorfismo de sobreposição e sobrecarga.

E duas obrigatoriedades(2 componentes):
Atributos e Metodos.
Atributos: São sinonimos de variáveis(Exemplo: Um carro possui portas, rodas...).
Metodos: São sinonimos de funções(Exemplo: Um carro liga, anda, acelera...)

O primeiro

Instância(Instanciar um objeto)
Criar um objeto atráves de uma classe
O que é um objeto?
Uma instância da classe.

Programação Estrutural, funcional, orientada a objetos"""