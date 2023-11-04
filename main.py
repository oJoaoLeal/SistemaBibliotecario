from Model.Emprestimo import Emprestimo
from Model.Livro import Livro
from Model.Usuario import Usuario


def mostrar_menu():
    print("### Menu de Opções ###")
    print("1. Listar Livros")
    print("2. Listar Empréstimos")
    print("3. Sair")


if __name__ == '__main__':
    usuario = Usuario()
    usuario.set_login(input("Login: "))
    usuario.set_senha(input("Senha: "))

    if usuario.validar_acesso():
        print(f"Acesso permitido! Bem vindo(a) {usuario.get_nome()}.")

        while True:
            mostrar_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("Você escolheu a opção de listar livros.")

                Livro.listar_livros()

            elif opcao == "2":
                print("Você escolheu a opção de listar empréstimos.")
                Emprestimo.listar_emprestimos()

            elif opcao == "3":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    else:
        print("Acesso Negado! Login ou senha inválidos.")
