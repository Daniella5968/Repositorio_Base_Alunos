class Pássaro():

    def __init__(self, tamanho, cores, especie, sexo):
        self.tamanho=tamanho
        self.cores=cores
        self.especie=especie
        self.sexo=sexo

    def cantar(self):
        return print(f'sou um {self.especie} cantando uma bela cancao')
        
    def voar(self):
        return print('Batendo as asas e: voando...')
    
passaro1 = Pássaro(0.14,['Marrom', 'Branco', 'cinza'],'pardal','M')
passaro1.cantar()
    
passaro2 = Pássaro(1.15,['Preto'], 'corvo','M')
passaro2.cantar()
passaro2.voar()
passaro3 = Pássaro(0.55,['Azul'], 'Arara', 'M', 'Rio de janeiro')
passaro3.cantar()
passaro3.voar()


