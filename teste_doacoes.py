# --- CONFIGURAÇÃO INICIAL ---
categorias = ("Roupa", "Alimento", "Brinquedo") # Tupla 

# Dicionário de necessidades por região 
necessidades = {
    "Norte": {"Roupa": "Estável", "Alimento": "Urgente", "Brinquedo": "Médio"},
    "Sul": {"Roupa": "Urgente", "Alimento": "Estável", "Brinquedo": "Médio"},
    "Centro": {"Roupa": "Médio", "Alimento": "Médio", "Brinquedo": "Urgente"}
}
lista_doacoes = [] 

print("-"*42)
print("--- SISTEMA DE DOAÇÕES INTELIGENTE ABP ---")
print("-"*42)

while True:
    print("\n O que deseja doar?")
    for i, categoria in enumerate(categorias):
        print(f"{i+1} - {categoria}")
    
    opcao = int(input("Escolha o número: "))
    cadastro = {}
    
    # 1. Definimos a categoria e a região primeiro
    if opcao == 1:
        categoria_nome = "Roupa"
        regiao_destino = "Sul"
    elif opcao == 2:
        categoria_nome = "Alimento"
        regiao_destino = "Norte"
    elif opcao == 3:
        categoria_nome = "Brinquedo"
        regiao_destino = "Centro"
    else:
        print("Opção inválida!")
        continue

    # 2. Pegamos o status PADRÃO da região (Agora fora do if/elif para não repetir código)
    status_especifico = necessidades[regiao_destino][categoria_nome]

    # 3. Aplicamos as perguntas extras e as mudanças de urgência
    if opcao == 1:
        estado = input("Qual o estado da roupa? (bom/estável/precisa ajuste): ").strip().lower()
        cadastro.update({"estado_item": estado})
    
    elif opcao == 2:
        vencendo = input("O alimento está perto do vencimento? (S/N): ").strip().upper()
        if vencendo == "S":
            status_especifico = "CRÍTICO (Vencimento Próximo!)" # Aqui ele altera o padrão
        cadastro.update({"alerta_vencimento": vencendo})

    item = input(f"Qual o item de {categoria_nome}? ").strip().lower()
    
    # 4. Salvamos tudo no dicionário final
    cadastro.update({
        "categoria": categoria_nome, 
        "item": item, 
        "regiao": regiao_destino,
        "urgencia": status_especifico
    })
    
    lista_doacoes.append(cadastro)
    print(f"\n✅ Destino definido: Sua doação de {item} será enviada para o {regiao_destino}.")
    print(f"Motivo: A necessidade de {categoria_nome} lá é {status_especifico}!")

    continuar = input("\nDeseja cadastrar outra doação? (S/N): ").upper()
    if continuar == "N":
        break

# --- RESUMO FINAL ---
print("\n--- RELATÓRIO DE LOGÍSTICA DE DOAÇÕES ---")
for d in lista_doacoes:
    print(f"Item: {d['item']} -> {d['regiao']} (Status: {d['urgencia']})")