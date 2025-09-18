import csv
exemplo = open('OCORRENCIAS_2025.csv')
leitor = csv.reader(exemplo, delimiter=';')
total_Espingarda = 0
total = Garrucho = 0
total = Pistola = 0
total = Pistolao = 0
total = Revolver = 0
total = Rifle = 0
total = Carabina = 0
total = Carabina_Fuzil = 0
total = Carabina_Cartucheira = 0
total = Pistola = 0

for linha in leitor:
    if linha[4].strip() == "Espingarda":
        total_Espingarda = total_Espingarda + 1
    elif linha[4].strip() == "Pistola":
        total_pistola = total_pistola + 1
    elif linha[4].strip() == "pistolao":
        total_pistolao = total_pistolao + 1
    elif linha[4].strip() == "pistolao":
        total_pistolao = total_pistolao + 1
    elif linha[4].strip() == "Revolver":
        total_Revolver = total_Revolver + 1
    elif linha[4].strip() == "Rifle":
        total_Rifle = total_Rifle + 1
        

