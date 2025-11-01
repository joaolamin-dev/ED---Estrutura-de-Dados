from collections import deque

def menu():
    print("\n=== MENU PLAYLIST DE MÚSICAS ===")
    print("1 - Adicionar música à playlist")
    print("2 - Tocar próxima música")
    print("3 - Mostrar playlist")
    print("4 - Sair")

def main():
    playlist = deque()  # Estrutura FIFO para a playlist

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            musica = input("Digite o nome da música: ").strip()
            if musica:
                playlist.append(musica)
                print(f"A música '{musica}' foi adicionada à playlist.")
            else:
                print("Nome inválido. Tente novamente.")

        elif opcao == "2":
            if playlist:
                tocando = playlist.popleft()
                print(f"Tocando agora: 🎶 {tocando}")
            else:
                print("A playlist está vazia. Adicione músicas primeiro.")

        elif opcao == "3":
            if playlist:
                print("\nMúsicas na playlist:")
                for i, musica in enumerate(playlist, start=1):
                    print(f"{i}. {musica}")
            else:
                print("A playlist está vazia.")

        elif opcao == "4":
            print("Encerrando o programa... Até a próxima sessão musical! 🎧")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
