import os

os.system("cls")

def adicionar_treino():
    data = input("Digite a data do treino (AAAA-MM-DD): ")
    distancia = float(input("Digite a distância percorrida (em km): "))
    tempo = input("Digite o tempo do treino (HH:MM:SS): ")
    localizacao = input("Digite a localização do treino: ")
    condicoes_climaticas = input("Digite as condições climáticas: ")
    
    with open("treinos.txt", "a") as arquivo:
        arquivo.write(f"{data},{distancia},{tempo},{localizacao},{condicoes_climaticas}\n")

    print("Treino adicionado com sucesso!")

def visualizar_treinos():
    try:
        with open("treinos.txt", "r") as arquivo:
            treinos = arquivo.readlines()

            if treinos:
                print("\n--- Treinos Registrados ---")
                for treino in treinos:
                    data, distancia, tempo, localizacao, condicoes_climaticas = treino.strip().split(",")
                    print(f"Data: {data}, Distância: {distancia} km, Tempo: {tempo}, Localização: {localizacao}, Condições Climáticas: {condicoes_climaticas}")
            else:
                print("Nenhum treino registrado.")
    except FileNotFoundError:
        print("Arquivo de treinos não encontrado.")

def filtrar_treinos():
    opcao = input("Digite (1) para filtrar por distância: ")

    if opcao == "1":
        distancia_minima = float(input("Digite a distância mínima (em km): "))
        distancia_maxima = float(input("Digite a distância máxima (em km): "))

        with open("treinos.txt", "r") as arquivo:
            treinos = arquivo.readlines()

            print("\n--- Treinos Filtrados ---")
            for treino in treinos:
                data, distancia, tempo, localizacao, condicoes_climaticas = treino.strip().split(",")
                distancia = float(distancia)
                if distancia_minima <= distancia <= distancia_maxima:
                    print(f"Data: {data}, Distância: {distancia} km, Tempo: {tempo}, Localização: {localizacao}, Condições Climáticas: {condicoes_climaticas}")
    else:
        print("Opção inválida.")

def definir_metas():
    metas = {}
    print("\n--- Definir Metas ---")
    metas["distancia_total"] = float(input("Digite a distância que deseja percorrer (em km): "))
    metas["tempo_total"] = input("Digite o tempo que deseja para percorrer essa distância (HH:MM:SS): ")

    with open("metas.txt", "w") as arquivo:
        for chave, valor in metas.items():
            arquivo.write(f"{chave},{valor}\n")

    print("\nMetas definidas com sucesso!")

def visualizar_metas():
    try:
        with open("metas.txt", "r") as arquivo:
            metas = arquivo.readlines()
            print("\n--- Metas Atuais ---")
            metas_dict = {meta.split(",")[0]: meta.split(",")[1].strip() for meta in metas}
            
            distancia = metas_dict.get("distancia_total", "Não definida")
            tempo = metas_dict.get("tempo_total", "Não definido")
            
            print(f"Distância desejada: {distancia} km")
            print(f"Tempo desejado para a distância: {tempo}")
    except FileNotFoundError:
        print("Nenhuma meta definida ainda.")

def verificar_progresso():
    try:
        with open("treinos.txt", "r") as arquivo_treinos, open("metas.txt", "r") as arquivo_metas:
            treinos = arquivo_treinos.readlines()
            metas = {meta.split(",")[0]: meta.split(",")[1].strip() for meta in arquivo_metas.readlines()}

            distancia_total = sum(float(treino.split(",")[1]) for treino in treinos)
            meta_distancia = float(metas.get("distancia_total", 0))

            print("\n--- Progresso em Relação às Metas ---")
            print(f"Meta de distância: {meta_distancia} km")
            print(f"Distância percorrida: {distancia_total:.2f} km")
            if distancia_total >= meta_distancia:
                print("Parabéns! Você alcançou sua meta de distância.")
            else:
                print(f"Faltam {meta_distancia - distancia_total:.2f} km para atingir sua meta.")
    except FileNotFoundError:
        print("Dados insuficientes para calcular o progresso.")

def atualizar_metas():
    try:
        metas = {}
        metas["distancia_total"] = float(input("Digite a nova meta de distância total (em km): "))
        metas["tempo_5km"] = input("Digite a nova meta de tempo para 5 km (HH:MM:SS): ")

        with open("metas.txt", "w") as arquivo:
            for chave, valor in metas.items():
                arquivo.write(f"{chave},{valor}\n")

        print("\nMetas atualizadas com sucesso!")
    except ValueError:
        print("Erro ao atualizar as metas.")
