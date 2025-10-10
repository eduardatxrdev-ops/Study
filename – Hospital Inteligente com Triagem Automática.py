import os 
import random
os.system("Cls")

pacientes = []
medicos = []
total_leitos = 10  
leitos_ocupados = 0

while True:
    print("=====Menu=====")
    print("1 - Cadastrar paciente")
    print("2 - Cadastrar Médico")
    print("3 - Exibir Fila de triagem")
    print("4 - Médicos Cadastrados")
    print("5 - Calcular tempo médio de espera")
    print("6 - Exibir Leitos disponíveis")
    print("7 - Médicos com Mais atendimentos")
    print("8 - Sair")
    
    opcao = input("Digite uma opção: ")
    
    if opcao == "1":
        print ("=====Cadastro de Pacientes=====")
        if leitos_ocupados < total_leitos: 
            id_paciente = len(pacientes) + 1
            nome = input("Digite o seu nome: ")
            nascimento = input("Digite a sua data de nascimento: ")
            telefone = float(input("Digite o seu telefone: "))
            email = input("Digite o seu email: ")
            
            print("---Endereço---")
            rua = input("Digite a sua rua: ")
            bairro = input ("Digite o seu bairro: ")
            cidade = input ("Digite a cidade: ")
            cep = int(input ("Digite Cep da sua residência: "))
        
            gravidade = int(input("Gravidade (1-Leve / 2-Moderado / 3-Grave): "))
            
            if leitos_ocupados < total_leitos:
                # Permitir cadastro
                id_paciente = len(pacientes) + 1

            if gravidade == 3:  
                #grave
                tempo_espera = 5
            elif gravidade == 2: #Moderado
                tempo_espera = 20
            else:                #Leve
                tempo_espera = 40
            
            paciente = {
                "id": id_paciente,
                "nome": nome,
                "nascimento": nascimento,
                "telefone": telefone,
                "email": email,
                "endereco": {"rua": rua, "bairro": bairro, "cidade": cidade, "cep": cep},
                "gravidade": gravidade,
                "tempo_espera": tempo_espera,
                "status": "esperando" }
               
            pacientes.append(paciente);
            leitos_ocupados += 1;  # Atualiza leitos ocupados
            print(f"Paciente {nome} cadastrado com sucesso! Leitos ocupados {leitos_ocupados}/{total_leitos}")
    
        else:
            print("Não há leitos disponíveis no momento!")

        
    elif opcao =="2":
        print ("=====Cadastro de Médicos=====")
        id_medico = len(medicos) + 1
        nome = input("Digite o nome: ")
        especialidade = input("Digite a Especialidade: ")
        
        medico ={
            "id":id_medico,
            "nome":nome,
            "especialidade": especialidade,
            "quantidade_atendimentos": 0
        }
        medicos.append(medico)
        print(f"Médico {nome} cadastrado com sucesso!")
   
    elif opcao == "3":
        if len(pacientes) == 0:
            print("\nNenhum paciente cadastrado.")
        else:
            # Separar por gravidade
            graves = []
            moderados = []
            leves = []

            for p in pacientes:
                if p["gravidade"] == 3:
                    graves.append(p)
                elif p["gravidade"] == 2:
                    moderados.append(p)
                else:
                    leves.append(p)

            # Juntar as listas na ordem correta (fora do for)
            fila_ordenada = graves + moderados + leves
        
            
        print("\n===== Fila de Triagem =====")
        for p in fila_ordenada:
            print(f"ID: {p['id']} | Nome: {p['nome']} | Gravidade: {p['gravidade']} | Tempo de espera: {p['tempo_espera']} min | Status: {p['status']}")
           
    elif opcao == "4":
        if len(medicos) == 0:
            print("Nenhum médico cadastrado.")
        else:
            print("===== Médicos Cadastrados =====")
        for m in medicos:   # <-- corrigido
            print(f"ID: {m['id']} | Nome: {m['nome']} | Especialidade: {m['especialidade']} | Atendimentos: {m['quantidade_atendimentos']}")

    
    elif opcao == "5":
        if len(pacientes) == 0:
            print("\nNenhum paciente cadastrado.")
        else:
            total_espera = 0
            for p in pacientes:
                total_espera += p["tempo_espera"]
            media = total_espera / len(pacientes)
            print(f"\nTempo médio de espera: {media:.2f} minutos")
    
    elif opcao =="6":
        leitos_disponiveis = total_leitos - leitos_ocupados
        print(f"\nLeitos ocupados: {leitos_ocupados}/{total_leitos}")
        print(f"Leitos disponíveis: {leitos_disponiveis}/{total_leitos}")
    elif opcao == "7":
        if len(medicos) == 0:
            print("Nenhum médico cadastrado.")
        else:
            # Criar uma cópia da lista para ordenar
            ranking = medicos[:]

            # Bubble sort simples: maior quantidade de atendimentos primeiro
            for i in range(len(ranking)):
                for j in range(0, len(ranking)-i-1):
                    if ranking[j]["quantidade_atendimentos"] < ranking[j+1]["quantidade_atendimentos"]:
                        ranking[j], ranking[j+1] = ranking[j+1], ranking[j]

            print("\n===== Ranking de Médicos =====")
            for m in ranking:
                print(f"ID: {m['id']} | Nome: {m['nome']} | Especialidade: {m['especialidade']} | Atendimentos: {m['quantidade_atendimentos']}")
                
    elif opcao == "8":
        print("\nSaindo do sistema...")
        break
    
    else:
        print("\nOpção inválida! Tente novamente.")
