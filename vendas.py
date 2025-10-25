vendas ={}

def processar_venda():
    codigo_produto = input("Digite o código do produto a ser vendido: ")
    quantidade_vendida = int(input("Digite a quantidade a ser vendida: "))
    preco_unitario = float(input("Digite o preço unitário do produto: "))
                                   
    # Aqui você pode adicionar a lógica para processar a venda,
    # como verificar o estoque, atualizar quantidades, calcular total, etc.
    total_da_compra = preco_unitario * quantidade_vendida
    print(f"Venda processada. Total da compra: R$ {total_da_compra:.2f}")
    
    # Verifica se o produto existe e se há quantidade suficiente
    # if codigo_produto not in produto:
    #     print("Produto não encontrado.")
    #     return
    # if quantidade_vendida > produto[codigo_produto]['quantidade']:
    #     print("Estoque insuficiente.")
    #     return
    #
    # Atualiza o estoque
    # produto[codigo_produto]['quantidade'] -= quantidade_vendida
