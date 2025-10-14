class Personagem:
    def __init__(self, Daniella, quinze, vida, forca, vivo=True):
        self.nome = Daniella
        self.idade = quinze
        self.vida = vida
        self.vivo = vivo
        self.forca = forca

    def atacar(self, dano):
        """Simula um ataque."""
        print(f"{self.nome} atacou causando {dano} de cano!")

    def defender(self, dano_recebido):
        """Reduz vida ao defender de um ataque."""
        self.vida -= dano_recebido
        print(f"{self.nome} defendeu, mas perdeu {dano_recebido} de vida!")
        self.morrer()

    def curar(self, valor):
        """Recuperar pontos de vida."""
        self.vida += valor
        print(f"{self.nome} se curou em {valor} pontos. vida atual: {self.vida}")

    def morrer(self):
        """Define que o  personagem morreu."""
        self.vivo = False
        self.vida
        print(f"{self.nome} morreu")

    def status(self):
        """Exibe informacao do personagem"""
        print("=== STATUS do personagem ===") 
        print(f"Nome:{self.nome}")
        print(f"idade:{self.idade}")
        print(f"vida:{self.vida}")
        print(f"forca:{self.forca}")
        print(f"vivo{'sim' if self.vivo else 'nao'}")