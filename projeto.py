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
