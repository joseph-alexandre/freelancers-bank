from config import *
from models import Projeto


@app.route("/")
def home():
    return "Bem-vindo(a) ao Back-end."


@app.route("/listar_projetos")
def listar_projetos():
    projetos = db.session.query(Projeto).all()
    retorno = []
    for p in usuarios:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route("/incluir_projeto", methods=['post'])
def incluir_projeto():
    dados = request.get_json()
    novo_projeto = Projeto(**dados)
    db.session.add(novo_projeto)
    db.session.commit()
    return Response('{"result": "Projeto criado com sucesso."}', status=200, mimetype='application/json')


app.run(debug=True)
