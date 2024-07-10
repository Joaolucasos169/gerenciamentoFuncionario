# João Lucas Oliveira;
# Mateus Nunes;
# Vanessa Ferreira.

class Funcionario():
    def __init__ (self, nome, cargo, salario,):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def __str__(self):
        return f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario}"

f1 = Funcionario("João", "Estágiario T.I", 4000)
f2 = Funcionario("Vanessa", "Recepcionista", 6000)
f3 = Funcionario("Mateus", "Auxiliar Administrativo", 10000)
f4 = Funcionario("Manoel", "Analista de Sistemas", 2000)

funcionarios = [f1,f2,f3,f4]

# Funções de cada de opção.
def adicionar_funcionario():
    nome = input("Digite o nome do novo funcionário: ")
    cargo = input("Digite o cargo do novo funcionário: ")
    salario = float(input("Digite o salário do novo funcionário: "))

    novo_funcionario = Funcionario(nome, cargo, salario)
    funcionarios.append(novo_funcionario)
    print("Funcionário adicionado com sucesso!")
    
def remover_funcionario():
    nome_final = input("Digite o nome do funcionário que deseja remover: ").lower()

    for funcionario in funcionarios:
        if funcionario.nome.lower() == nome_final :
            funcionarios.remove(funcionario)
            print("Funcionário removido com sucesso!")
            return

    print("Funcionário não encontrado!")
    
    
def listar_funcionarios():
    print("\nLista de Funcionários:")
    for funcionario in funcionarios:
        print(funcionario)
        
def editar_funcionario():
    nome_final = input("Digite o nome do funcionário que deseja alterar: ").lower()
    for funcionario in funcionarios:
        if funcionario.nome.lower() == nome_final:
            
            novo_nome = input("Novo nome: ")
            novo_cargo = input("Novo cargo: ")
            novo_salario = float(input("Novo salário: "))

            funcionario.nome = novo_nome
            funcionario.cargo = novo_cargo
            funcionario.salario = novo_salario

            print("Informações do funcionário atualizadas com sucesso!")
            return

    print("Funcionário não encontrado!")

# Menu de opções com as condicionais.
while True:
    print('''Escolha uma opção:
    1 - Adicionar um funcionário.
    2 - Remover um funcionário.
    3 - Ver lista de funcionários.
    4 - Alterar informações de um funcionário.
    5 - Sair.
    ''')
    
    opcao = int(input("Opção: "))

    if opcao == 1:
        print("1")
        adicionar_funcionario()
    elif opcao == 2:
        print("2")
        remover_funcionario()
    elif opcao == 3:
        print("3")
        listar_funcionarios()
    elif opcao == 4:
        print("4")
        editar_funcionario()
    elif opcao == 5:
        print("5")
        print("Encerrando o programa...")
        break
    else:
        print("6")
        print("Opção inválida. Tente novamente.")
        
        
    