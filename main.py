import os

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("-------------------------------------------------")
    print("  Escolha a aplicação a ser executada:")
    print("-------------------------------------------------")
    print("1. Scraper de Notícias (G1)")
    print("2. Bot de Login e Scraper de Bio (Instagram)")
    print("3. Sair")
    print("-------------------------------------------------")

def main():
    """Função principal que gerencia a escolha do usuário."""
    while True:
        exibir_menu()
        escolha = input("Digite o número da sua escolha: ")

        if escolha == '1':
            print("\nExecutando Scraper de Notícias...\n")
            os.system('python ./noticias/scraper_noticias.py')
            print("\nExecução do Scraper de Notícias concluída.")
        elif escolha == '2':
            print("\nExecutando Bot do Instagram...\n")
            os.system('python ./instagram/bot_instagram.py')
            print("\nExecução do Bot do Instagram concluída.")
        elif escolha == '3':
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida. Por favor, tente novamente.\n")

if __name__ == "__main__":
    main()