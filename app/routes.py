from flask import render_template, request, redirect, url_for
from app import app

# --- DADOS (Mantidos conforme Aula 11 e Passo 1) ---
categorias = ("Roupa", "Alimento", "Brinquedo")
necessidades = { 
    "Norte": {"Roupa": "Estável", "Alimento": "Urgente", "Brinquedo": "Médio"}, 
    "Sul": {"Roupa": "Urgente", "Alimento": "Estável", "Brinquedo": "Médio"}, 
    "Centro": {"Roupa": "Médio", "Alimento": "Médio", "Brinquedo": "Urgente"} 
}
lista_doacoes = []

# --- LÓGICA (Sua função adaptada do Passo 1) ---
def processar_doacao(opcao, nome_item, info_extra):
    opcao = int(opcao)
    if opcao == 1:
        cat_nome, regiao_destino = "Roupa", "Sul"
    elif opcao == 2:
        cat_nome, regiao_destino = "Alimento", "Norte"
    elif opcao == 3:
        cat_nome, regiao_destino = "Brinquedo", "Centro"
    else:
        return None

    status_final = necessidades[regiao_destino][cat_nome]
    
    # Lógica de vencimento (Aula 05 e Aula 11)
    if cat_nome == "Alimento" and info_extra.upper() == "S":
        status_final = "CRÍTICO (Vencimento Próximo!)"
    
    return {
        "categoria": cat_nome, "item": nome_item.strip().lower(),
        "regiao": regiao_destino, "urgencia": status_final, "detalhe": info_extra 
    }

# --- ROTAS ---

@app.route('/')
@app.route('/index')
def index():
    # Passamos a lista para o HTML poder mostrar o relatório final depois
    return render_template('index.html', doacoes=lista_doacoes)

@app.route('/doar', methods=['GET', 'POST']) # Aceita ver a página e enviar dados
def doar():
    if request.method == 'POST':
        # 1. Pegamos os dados do formulário HTML
        item = request.form.get('item_nome')
        opcao = request.form.get('categoria_opcao')
        detalhe = request.form.get('detalhe')

        # 2. Chamamos sua função de lógica
        nova_doacao = processar_doacao(opcao, item, detalhe)

        # 3. Guardamos na lista (conforme Aula 09 e 11)
        if nova_doacao:
            lista_doacoes.append(nova_doacao)
            print(f"✅ Sucesso! {item} cadastrado.") # Aparece no seu terminal

        return redirect(url_for('index')) # Volta para o início após doar
    
    return render_template('doar.html')