class Empregado:
    def __init__(self, identificador, nome, cargo, alergias, problemas_medicos, telefone, email):
        self.identificador = identificador
        self.nome = nome
        self.cargo = cargo
        self.alergias = alergias
        self.problemas_medicos = problemas_medicos
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return (f"ID: {self.identificador}\n"
                f"Nome: {self.nome}\n"
                f"Cargo: {self.cargo}\n"
                f"Alergias: {self.alergias}\n"
                f"Problemas Médicos: {self.problemas_medicos}\n"
                f"Telefone: {self.telefone}\n"
                f"E-mail: {self.email}\n")


class GerenciadorDeEmpregados:
    def __init__(self):
        self.empregados = {}

    def adicionar_empregado(self):
        identificador = input("Digite o ID do empregado: ")
        nome = input("Digite o nome do empregado: ")
        cargo = input("Digite o cargo do empregado: ")
        alergias = input("Digite as alergias do empregado: ")
        problemas_medicos = input("Digite os problemas médicos do empregado: ")
        telefone = input("Digite o telefone do empregado: ")
        email = input("Digite o e-mail do empregado: ")

        empregado = Empregado(identificador, nome, cargo, alergias, problemas_medicos, telefone, email)
        self.empregados[identificador] = empregado
        print("Empregado adicionado com sucesso!")

    def buscar_empregado(self):
        identificador = input("Digite o ID do empregado para buscar suas informações: ")
        empregado = self.empregados.get(identificador)
        if empregado:
            print(empregado)
        else:
            print("Empregado não encontrado.")

    def executar(self):
        while True:
            print("\n1. Adicionar Empregado")
            print("2. Buscar Empregado")
            print("3. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.adicionar_empregado()
            elif escolha == '2':
                self.buscar_empregado()
            elif escolha == '3':
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    gerenciador = GerenciadorDeEmpregados()
    gerenciador.executar()
