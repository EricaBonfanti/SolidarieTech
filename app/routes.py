from flask import render_template, request, redirect, url_for
from app import app

# DADOS - Dicionário e Tupla
categorias = ("Roupa", "Alimento", "Brinquedo")
necessidades = { 
    "Norte": {"Roupa": "Estável", "Alimento": "Urgente", "Brinquedo": "Médio"}, 
    "Sul": {"Roupa": "Urgente", "Alimento": "Estável", "Brinquedo": "Médio"}, 
    "Centro": {"Roupa": "Médio", "Alimento": "Médio", "Brinquedo": "Urgente"} 
}
lista_doacoes = []

# LÓGICA - If, Elif, Else
def processar_doacao(opcao, nome_item, info_extra):
    opcao = int(opcao)
    if opcao == 1:
        categoria_nome, regiao_destino = "Roupa", "Sul"
    elif opcao == 2:
        categoria_nome, regiao_destino = "Alimento", "Norte"
    elif opcao == 3:
        categoria_nome, regiao_destino = "Brinquedo", "Centro"
    else:
        return None # retorna erro "opção inválida"

    status_final = necessidades[regiao_destino][categoria_nome]
    
    # Lógica do vencimento
    if categoria_nome == "Alimento" and info_extra.upper() == "S":
        status_final = "CRÍTICO (Vencimento Próximo!)"
    
    return {
        "categoria": categoria_nome, "item": nome_item.strip().lower(),
        "regiao": regiao_destino, "urgencia": status_final, "detalhe": info_extra 
    }

# ROTAS

@app.route('/')
@app.route('/index')
def index():
    # Passamos a lista para o HTML poder mostrar o relatório final depois
    return render_template('index.html', doacoes=lista_doacoes)

@app.route('/doar', methods=['GET', 'POST']) # GET e POST pois tem os dois
def doar():
    if request.method == 'POST':
        # 1. Pegando os Dados do formulário HTML
        item = request.form.get('item_nome')
        opcao = request.form.get('categoria_opcao')
        detalhe = request.form.get('detalhe')

        # 2. Chamando a função em lógica
        nova_doacao = processar_doacao(opcao, item, detalhe)

        # 3. Informação guardada na lista 
        if nova_doacao:
            lista_doacoes.append(nova_doacao)
            print(f"✅ Sucesso! {item} cadastrado.") # Aparece no terminal a mensagem

        return redirect(url_for('index')) # Volta para o início após doar
    
    return render_template('doar.html')