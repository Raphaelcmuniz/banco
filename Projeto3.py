class Banco:
    from time import sleep
    from random import randint

    lista_clientes = []             # Lista que contem dicionários com chaves: nome, conta, senha, saldo e cpf >> Cada índice dessa lista é uma pessoa que possui uma conta.
    contas_cliente = {}             #  nome, conta, senha, saldo e cpf. Armazena as informações
    conta = []                      # Toda nova conta gerada virá para cá com o intuito de garantir que não terão contas repetidas
    senhas = []                     # Toda nova senha gerada virá para cá com o intuito de garantir que não terão senhas repetidas
    la = []                         # Auxilia no print "Login ou Senha inválidos" no "menu()"

    num = 0                         # Auxilia a "lista_clientes" a manter o mesmo índice, assim, ajudando a sempre tratar da mesma pessoa
    aux = 0

    def menu(self):
        while True:
            print()
            print("=" * 15, "Banco Real", "=" * 15)
            print(''' 
            [1] Criar conta
            [2] Acessar conta
            [3] Sair''')
            opcao = input("> ")

            if opcao == '1':
                self.criar_conta()

            elif opcao == '2':
                if len(self.lista_clientes) >= 1:
                    while True:
                        login = int(input("Número da conta: "))
                        senha = int(input("Senha: "))
                        for c, e in enumerate(self.lista_clientes):
                            if login == self.lista_clientes[c]['conta'] and senha == self.lista_clientes[c]['senha']:
                                self.la.append('a')
                                self.num = c

                        if len(self.la) == 1:
                            self.la.clear()
                            self.acessar_conta()
                            break
                        else:
                            print()
                            print("**login ou senha incorretos**")
                            self.sleep(1.5)
                            print()
                else:
                    print()
                    print(">> Não existem contas cadastradas")
                    self.sleep(1)

            elif opcao == '3':
                break

            else:
                print(" "*10, "**Comando inválido**")
                self.sleep(1)

    def criar_conta(self):

        self.contas_cliente['nome'] = str(input("Nome completo: ")).title()
        while True:
            num = self.randint(1111, 9999)
            if num not in self.conta:
                self.conta.append(num)
                self.contas_cliente['conta'] = num
                break
        self.contas_cliente['cpf'] = int(input("CPF: "))
        while True:
            self.contas_cliente['senha'] = int(input("Senha: "))
            if self.contas_cliente['senha'] not in self.senhas:
                self.senhas.append(self.contas_cliente['senha'])
                self.contas_cliente['saldo'] = 0
                self.lista_clientes.append(self.contas_cliente.copy())
                break
            else:
                self.sleep(1)
                print("**Senha já existentente**")
                self.sleep(1.5)
                print("Faça uma nova tentativa")
                self.sleep(1.5)
        print()
        print("Gerando número de conta...")
        self.sleep(2)
        print()
        print(f"Núnero da conta: {self.contas_cliente['conta']}")

    def acessar_conta(self):
        while True:
            lay = len(self.lista_clientes[self.num]['nome']) + 15
            tam = '='*lay
            print()
            print(tam, "Banco Real", tam)
            print()
            print(f"Nome: {self.lista_clientes[self.num]['nome']}", " "*(lay + 8), f"Conta: {self.lista_clientes[self.num]['conta']}")
            print(''' 
[1] Saldo
[2] Depósito
[3] Saque
[4] Transferência
[5] Sair''')
            opcao = input("> ")

            if opcao == '1':
                self.exibe_saldo()

            elif opcao == '2':
                self.depositar()

            elif opcao == '3':
                self.sacar()

            elif opcao == '4':
                self.transferir()

            elif opcao == '5':
                break

            else:
                print("**Comando inválido**")

    def exibe_saldo(self):
        print()
        print("Seu saldo é de: {0:.2f} R$".format(self.lista_clientes[self.num]['saldo']))

    def depositar(self):
        print("Quanto deseja depositar?")
        g = float(input("> "))
        print()
        print("Depositando...")
        self.sleep(1.5)
        print("=" * 20)
        print()
        print("Operação realizada com sucesso!")
        print()
        self.lista_clientes[self.num]['saldo'] += g

    def sacar(self):
        print("Quanto deseja sacar?")
        x = float(input("> "))
        if self.lista_clientes[self.num]['saldo'] >= x:
            print()
            print("Sacando...")
            self.sleep(1.5)
            print("=" * 20)
            print()
            print("Operação realizada com sucesso!")
            self.lista_clientes[self.num]['saldo'] -= x
        else:
            print()
            print("**Saldo insuficiente**")

    def transferir(self):
        t = float(input("Quanto deseja transferir?\n"))
        if self.lista_clientes[self.num]['saldo'] >= t:
            print("Deseja trasnferir para: ")
            while True:
                nome_transferencia = str(input("Nome: ")).title()
                cpf_transferencia = int(input("CPF: "))
                conta_transferencia = int(input("Conta: "))
                for c, e in enumerate(self.lista_clientes):
                    if nome_transferencia == self.lista_clientes[c]['nome'] and conta_transferencia == self.lista_clientes[c]['conta'] and cpf_transferencia == self.lista_clientes[c]['cpf']:
                        self.la.append('a')
                        self.aux = c

                if len(self.la) == 1:
                    self.la.clear()
                    self.lista_clientes[self.num]['saldo'] -= t
                    self.lista_clientes[self.aux]['saldo'] += t
                    break
                else:
                    print()
                    print("**Nome, Conta ou CPF inválidos**")
                    self.sleep(1.5)
                    tentar_novamente = input("Deseja tentar novamente? [S/N]\n")
                    if tentar_novamente in 'Ss':
                        continue
                    elif tentar_novamente in 'Nn':
                        break
                    else:
                        print("Digite apenas S ou N")
        else:
            print()
            print("**Saldo insuficiente**")


p = Banco()
p.menu()
