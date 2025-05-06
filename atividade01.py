from biblioteca import Pessoa

aluno01 = Pessoa("Guilherme", 21, 82)


print(f"{aluno01.nome} tem {aluno01.idade} anos e pesa {aluno01.peso} quilos.")

if aluno01.falar == aluno01.comer:
    print("Você não pode falar comendo")