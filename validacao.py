validacao = {}

def validar_data(data_str):
    from datetime import datetime
    try:
        data_valida = datetime.strptime(data_str, "%d/%m/%Y")  # ✅ strptime formata data -> data
        return data_valida.strftime("%d/%m/%Y") # ✅ strftime formata data -> string
    except ValueError:
        print("Data inválida. Use o formato DD/MM/AAAA.")
        return None