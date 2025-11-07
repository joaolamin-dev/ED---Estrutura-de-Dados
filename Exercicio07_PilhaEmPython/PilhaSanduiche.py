def mostrar_menu():
    print("\n=== MONTAGEM DO SEU SANDUÍCHE ===")
    print("1 - Adicionar ingrediente")
    print("2 - Remover ingrediente (do topo)")
    print("3 - Ver último ingrediente adicionado")
    print("4 - Mostrar sanduíche")
    print("5 - Finalizar pedido")

sanduiche = []

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ingrediente = input("Digite o nome do ingrediente: ").strip()
        if ingrediente:
            sanduiche.append(ingrediente)
            print(f"✅ {ingrediente} adicionado ao sanduíche!")
        else:
            print("⚠️ Ingrediente inválido!")

    elif opcao == "2":
        if sanduiche:
            removido = sanduiche.pop()
            print(f"❌ {removido} foi removido do topo do sanduíche.")
        else:
            print("⚠️ O sanduíche está vazio!")

    elif opcao == "3":
        if sanduiche:
            print(f"🍅 Último ingrediente adicionado: {sanduiche[-1]}")
        else:
            print("⚠️ O sanduíche ainda está vazio!")

    elif opcao == "4":
        if sanduiche:
            print("\n🍔 Seu sanduíche atual (de baixo para o topo):")
            for i, ingrediente in enumerate(sanduiche, start=1):
                print(f"{i}. {ingrediente}")
        else:
            print("⚠️ Nenhum ingrediente foi adicionado ainda.")

    elif opcao == "5":
        print("\n🥪 Pedido finalizado! Bom apetite!")
        break
    
    else:
        print("❌ Opção inválida! Tente novamente.")
