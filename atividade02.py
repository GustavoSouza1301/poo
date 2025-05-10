from biblioteca import ContaBancaria

minhaConta = ContaBancaria(123,"Gusta","corrente")


minhaConta.ativarConta()
minhaConta.depositar(100)
minhaConta.verificarSaldo()
minhaConta.sacar(50)
minhaConta.verificarSaldo()
minhaConta.desativarConta()
minhaConta.sacar(50)
minhaConta.verificarSaldo()
minhaConta.desativarConta()