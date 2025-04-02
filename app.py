from flask import Flask, request

app = Flask(__name__)

historico = []

@app.route('/perguntas', methods=["GET"])
def pergunta():
    return {
        'id': '1994',
        'pergunta': 'quanto é 2+2?'
    }

@app.route('/pergunta/<matricula>', methods=["POST"])
def calculos(matricula):
    pergunta_dados = request.get_json()
    numero1 = pergunta_dados['numero1']
    numero2 = pergunta_dados['numero2']
    resultado = numero1 + numero2

    historico.append({
        'matricula': matricula,
        'numero1': numero1,
        'numero2': numero2,
        'resultado': resultado
    })

@app.route('/perguntas/<matricula>/<id>', methods=["POST"])
def mandado(matricula, id):
    pergunta_resposta = request.get_json()
    resposta_aluno = pergunta_resposta['resposta']
    return {
        'matricula_aluno': matricula,
        'id_pergunta': id,
        'resposta_aluno': resposta_aluno
    }
