class Midia:
    def __init__(self,tiyulo: str,artista):
        self.Titulo=titulo
        self.Artista=artista
class Musica(Midia):
    def __repr__(self):
        return f"'{self.titulo}'por{self.artista}"
class Playlist:
    def __init__(self,nome: srt ,musicas:list[Musica]):
        self.nome=nome
        self.musicas=musicas

    def tocar_todas(self):
        print(f"\n tocando a paylist'{self.nome}'!")
        for musica in self.musicas:
            print(f" tocando agora:{musica}")

musica_1=Musica("jesus chorou, sao paulo,fabrica de bico","racionais Mc's")
musica_2=Musica("Aoa,Favela sinistra,partiu","Mc kekel")
musica_3=Musica("Mina de vermelho,tiger preta,por que o homem nao chora","Mc daleste")

daylist= "playlist" ("sua playlist diaria",
                 [musica_1,musica_2,musica_3])
print(musica_1)




        