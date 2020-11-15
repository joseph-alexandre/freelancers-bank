from config import *


class Projeto(db.Model):
    __tablename__ = 'projeto'
    id = Column(Integer, primary_key=True)
    nome = Column(String(200))
    caminho_imagem = Column(String())
    descricao = Column(String(300))
    nome_criador = Column(String(200))
    url_repositorio = Column(String(350))

    def __str__(self):
        return str(self.id) + ", " + self.nome + ", " + self.caminho_imagem + ", " + self.descricao + ", " + self.nome_criador + ", " + self.url_repositorio

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "caminho_imagem": self.caminho_imagem,
            "descricao": self.descricao,
            "nome_criador": self.nome_criador,
            "url_repositorio": self.url_repositorio
        }


if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()
