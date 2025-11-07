def mostrar_menu():
    print("\n=== HISTÓRICO DE NAVEGAÇÃO ===")
    print("1 - Visitar novo site")
    print("2 - Voltar (remover último site visitado)")
    print("3 - Ver site atual (último visitado)")
    print("4 - Mostrar todo o histórico")
    print("5 - Limpar histórico")
    print("6 - Sair")


historico = []

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        site = input("Digite o endereço do site (ex: www.exemplo.com): ").strip()
        if site:
            historico.append(site)
            print(f"🌐 Você visitou: {site}")
        else:
            print("⚠️ Endereço inválido!")

    elif opcao == "2":
        if historico:
            site_removido = historico.pop()
            print(f"⬅️ Você voltou do site: {site_removido}")
            if historico:
                print(f"🔸 Agora você está em: {historico[-1]}")
            else:
                print("🏠 Você voltou para a página inicial.")
        else:
            print("⚠️ Nenhum site no histórico!")

    elif opcao == "3":
        if historico:
            print(f"🔎 Site atual: {historico[-1]}")
        else:
            print("⚠️ Nenhum site visitado ainda.")

    elif opcao == "4":
        if historico:
            print("\n🕘 Histórico completo (do primeiro ao último):")
            for i, site in enumerate(historico, start=1):
                print(f"{i}. {site}")
        else:
            print("⚠️ O histórico está vazio.")

    elif opcao == "5":
        if historico:
            historico.clear()
            print("🧹 Histórico limpo com sucesso!")
        else:
            print("⚠️ O histórico já está vazio.")

    elif opcao == "6":
        print("\n👋 Saindo do navegador. Até mais!")
        break

    else:
        print("❌ Opção inválida! Tente novamente.")
