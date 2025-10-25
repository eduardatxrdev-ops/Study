import os
os.system ("Cls" if os.name == "nt" else "clear")
import produto as prod
import sessao
import validacao as val
import vendas 

def menu_principal():
    while True:
        print ("\n=== Sistema de Controle de Produtos em Supermercado ===")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Remover Produto")
        print("4. Processar Venda")
        print("5. Procurar Produto")
        print ("6. Valor Unitário do Produto")
        print ("7. Checar Validade do Produto")
        print("8. Sair")
        
        escolha = input("Escolha uma opção: ")
        while escolha not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Opção inválida. Tente novamente.")
            escolha = input("Escolha uma opção: ")
        if escolha == '1':
            codigo = input("Código do Produto: ")
            nome = input("Nome do Produto: ")
            sessao_nome = input("Sessão do Produto: ")
            valor_unitario = float(input("Valor Unitário: "))
            peso = float(input("Peso (kg): "))
            quantidade = int(input("Quantidade: "))
            data_de_validade = val.validar_data(input("Data de Validade (DD/MM/AAAA): "))
            prod.adicionar_produto(codigo, nome, sessao_nome, valor_unitario, peso, quantidade, data_de_validade)
        elif escolha == '2':
            prod.listar_produtos()  
        elif escolha == '3':
            codigo = input("Código do Produto a ser removido: ")
            prod.remover_produto(codigo)    
        elif escolha == '4':
            vendas.processar_venda()
        elif escolha == '5':
            codigo = input("Código ou nome do produto a ser procurado: ")
            encontrado = False
            for cod, detalhes in prod.produtos.items():
                if cod == codigo or detalhes['nome'].lower() == codigo.lower():
                    print(f"Código: {cod} | Nome: {detalhes['nome']} | Sessão: {detalhes['sessao']} | "
                        f"Valor Unitário: {detalhes['valor_unitario']:.2f} | Peso: {detalhes['peso']}kg | "
                        f"Quantidade: {detalhes['quantidade']} | Validade: {detalhes['data_de_validade']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Produto não encontrado.")

            print("Produto não encontrado.")
        elif escolha == '6':
                    codigo = input("Código do Produto para ver o valor unitário: ")
                    if codigo in prod.produto:
                        valor = prod.produto[codigo]['valor_unitario']
                        print(f"Valor Unitário do Produto {codigo}: R$ {valor:.2f}")
                    else:   
                        print("Produto não encontrado.") 
                        
        elif escolha == '7':
            codigo = input("Código do Produto para checar a validade: ")
            if codigo in prod.produto:
                data_de_validade = prod.produto[codigo]['data_de_validade']
                print(f"Data de Validade do Produto {codigo}: {data_de_validade}")
            else:   
                print("Produto não encontrado.")
        elif escolha == '8':
            print("Saindo do sistema. Até logo!")
            break
