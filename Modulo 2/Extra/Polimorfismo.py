este_dicionario = {
    "marca": "chevrolet",
    "modelo": "opala",
    "ano": 1969}

def comunicar(qualquer_animal):
    print(f"tentando comunicacao com {qualquer_animal.especie}")
    qualquer_animal.fazer_som()

class Passaro():
    def _init_(self, habitat, tamanho, cores, espectos, sexo):
        self.tamanho=tamanho
        self.cores=cores
        self.especie=espectos
        self.sexo=sexo
        self.habitat=habitat

    def cantar(self):
        return print(f'sou um {self.especie} cantandouma bela cancao')
    def voar(self):
        return print("Batendo as asas e: voando...")
    def fazer_som(self):
        return print(f"{self.especie} esta fazendo barulho")
    
    Passaro3=Passaro(0.14, {'preto', 'cinza'}, 'corvo', 'M', 'cemiterio')
    Passaro3.cantar()
    Passaro3.voar()
    Passaro3.habitat()
    Passaro3.fazer_som()
