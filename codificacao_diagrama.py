
class Artigo:
    def __init__(self, titulo_art, autor):
        self.titulo_art = titulo_art
        self.autor = autor
    
    def get_artigo(self):
        return "Titulo do artigo: " + self.titulo_art + "; " + "Autor do artigo: " + self.autor

class Edicao:
    def __init__(self, numero, volume, data):
        self.numero = numero
        self.volume = volume 
        self.data = data 
        self.artigos = []

    def get_edicao(self):
        return "Edição nº: " + str(self.numero) + "; " + "Volume: " + str(self.volume) + "; " + "Data: " + self.data 

    def add_artigo(self, artigo):
        self.artigos.append(artigo)
    
    def show_artigos(self):
        for artigo in self.artigos:
            print(artigo.get_artigo()) 

    def quant_artigos(self):
        return len(self.artigos) 

class Revista:
    def __init__(self, titulo_rev, issn, periodicidade):
        self.titulo_rev = titulo_rev
        self.issn = issn
        self.periodicidade = periodicidade
        self.edicoes = [] 

    def add_edicao(self, edicao):
        num_artigos = edicao.quant_artigos()
        if(num_artigos >= 10 and num_artigos <= 15):
            self.edicoes.append(edicao)
            return "Esta edição foi adicionada à revista!"
        else: 
            return "Para uma edição ser adicionada, deve conter no mínimo 10 artigos e no máximo 15." 

    def show_edicoes(self):
        for edicao in self.edicoes:
            print(edicao.get_edicao())
    
    def show_revista(self):
        return "Revista: " + self.titulo_rev + "; ISSN: " + str(self.issn) + "; Periodicidade: " + self.periodicidade   

#instanciando os objetos
#criação de 1 revista, 1 edição e 1 artigo
minha_revista = Revista("Tecnologia", "1", "trimestral")
edicao_revista = Edicao("1", "1", "01/03/2023")
artigo_1 = Artigo("Informática básica", "João Silva")

artigo_1.get_artigo()

#adicionando artigo_1 a edicao_revista
edicao_revista.add_artigo(artigo_1)

#tentar adicionar edicao_revista a minha_revista
minha_revista.add_edicao(edicao_revista)
edicao_revista.get_edicao()

#adicionando mais 9 artigos 
artigo_2 = Artigo("Internet", "Maria Silva")
artigo_3 = Artigo("Lógica e Linguagens de Programação", "Pedro Silva")
artigo_4 = Artigo("Manutenção de Computadores", "Catarina Silva")
artigo_5 = Artigo("Eletrônica", "Marcos Silva")
artigo_6 = Artigo("Páginas Web", "Solange Silva")
artigo_7 = Artigo("Arquitetura de Redes", "Rafael Silva")
artigo_8 = Artigo("Bancos de Dados", "Tiago Silva")
artigo_9 = Artigo("Aprendizado de máquina", "Joana Silva")
artigo_10 = Artigo("Tecnologia e sociedade", "Zefa Silva")
#adicionando os outros artigos a edicao_revista
edicao_revista.add_artigo(artigo_2)
edicao_revista.add_artigo(artigo_3)
edicao_revista.add_artigo(artigo_4)
edicao_revista.add_artigo(artigo_5)
edicao_revista.add_artigo(artigo_6)
edicao_revista.add_artigo(artigo_7)
edicao_revista.add_artigo(artigo_8)
edicao_revista.add_artigo(artigo_9)
edicao_revista.add_artigo(artigo_10)
#mostrando os artigos
edicao_revista.show_artigos()

#mostrar quantidade de artigos 
edicao_revista.quant_artigos()

#adicionar edicao_revista a minha_revista
minha_revista.add_edicao(edicao_revista)

#testar show_edicoes 
minha_revista.show_edicoes()

#testar show_revista
minha_revista.show_revista()