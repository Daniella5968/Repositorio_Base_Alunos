
class pessoa:
    def __init__(self, nome:str,disciplina:str):
        pass
        self.nome=nome
        self.disciplina=disciplina
        
class SalaDeAula:
    def __init__(self,numero:int,capacidade:int):
        self.numero=numero
        self.capacidade=capacidade
        print(f"sala{self.numero} esta disponivel.")

class Professor (pessoa):
    
    def dar_aula(self,sala:SalaDeAula):
        print(f"O Prof. {self.nome} de {self.disciplina}esta dando aula na sala{sala.numero}.")

sala_1=SalaDeAula(7,30)
prof_1=Professor("Lazaro","historia")
prof_1.dar_aula(sala_1)
