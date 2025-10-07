import json
import os

# Nome do arquivo onde os dados serão salvos
ARQUIVO = "vendedores.json"

# Verifica se o arquivo existe, se sim, carrega os dados
if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        vendedores = json.load(f)
else:
    vendedores = []  # lista vazia se for a primeira execução

while True:
    print("\n==== MENU ====")
    print("1 - Cadastrar vendedor")
    print("2 - Listar vendedores")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Cadastro de Vendedor ---")
        nome = input("Nome do vendedor: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")

        print("\n--- Endereço ---")
        rua = input("Rua: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")

        vendedor = {
            "id": len(vendedores) + 1,
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "endereco": {
                "rua": rua,
                "cidade": cidade,
                "estado": estado,
                "cep": cep
            }
        }

        # Adiciona o vendedor à lista
        vendedores.append(vendedor)

        # Salva no arquivo JSON
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(vendedores, f, ensure_ascii=False, indent=4)

        print(f"\n✅ Vendedor '{nome}' cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- Lista de Vendedores ---")
        if len(vendedores) == 0:
            print("Nenhum vendedor cadastrado ainda.")
        else:
            for v in vendedores:
                print(f"ID: {v['id']} | Nome: {v['nome']} | Cidade: {v['endereco']['cidade']}")

    elif opcao == "3":
        print("Encerrando o programa...")
        break

    else:
        print("❌ Opção inválida, tente novamente!")

