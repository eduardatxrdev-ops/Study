produto = {}

def adicionar_produto(codigo, nome, sessao, valor_unitario, peso, quantidade, data_de_validade):
    produto[codigo] = {
        'nome': nome,
        'sessao': sessao,
        'valor_unitario': valor_unitario,
        'peso': peso,
        'quantidade': quantidade,
        'data_de_validade': data_de_validade
    }
    print("Produto adicionado com sucesso.")

def listar_produtos():
    if not produto:
        print ("Nenhum produto cadastrado.")
        return
    for codigo, detalhes in produto.items():
        print(f"Código: {codigo} | Nome: {detalhes['nome']} | Sessão: {detalhes['sessao']} | "
              f"Valor Unitário: {detalhes['valor_unitario']} | Peso: {detalhes['peso']} | "
              f"Quantidade: {detalhes['quantidade']} | Data de Validade: {detalhes['data_de_validade']}")
        
def remover_produto(codigo):
    if codigo in produto:
        del produto[codigo]
        print("Produto removido com sucesso.")
    else: 
        print("Produto não encontrado.")
        
def procurar_produto(codigo):
    return produto.get(codigo, None)

def valor_unitario(codigo):
    if codigo in produto:
        input("Valor Unitário: ")
        return produto[codigo]['valor_unitario']
    else:
        print("Produto não encontrado.")