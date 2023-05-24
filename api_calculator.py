from flask import Flask, request, jsonify, render_template

app = Flask(__calculator__)

@app.route('/')
def index():
    return render_template('index.html')

def adicionar_linha_maior_oferta():
    tabela_lances = document.getElementById("lista_lances").getElementsByTagName("tbody")[0]
    maior_oferta = document.getElementById("valor_oferta").innerText

    nova_linha = "<tr>"
    nova_linha += f"<td><a href='#' rel='61560' class='excluir_lance'>Excluir</a></td>"
    nova_linha += "<td>Presencial</td>"
    nova_linha += "<td></td>"
    nova_linha += f"<td align='right'><strong>{maior_oferta}</strong></td>"
    nova_linha += "</tr>"

    # Inserir a nova linha no início da tabela
    tabela_lances.insertAdjacentHTML('afterbegin', nova_linha)


@app.route('/calcular', methods=['POST'])
def calcular():
    # Obtenha os dados do formulário do request
    valor_oferta = request.form.get('valor_oferta')
    # Faça o cálculo necessário
    resultado = float(valor_oferta) * 0.05
    # Retorne o resultado como uma resposta JSON
    return jsonify({'resultado': resultado})


def alterar_oferta(event):
    valor_atual = document.getElementById("valor_oferta").innerText
    novo_valor_atual = valor_atual.replace(/[^\d,-]/g, "")

    valor_oferta = event.target.innerHTML
    novo_valor_oferta = valor_oferta.replace(/[^\d,-]/g, "")

    novo_valor_atual = float(novo_valor_atual)
    novo_valor_oferta = float(novo_valor_oferta)
    diferenca = novo_valor_oferta - novo_valor_atual

    soma = diferenca + novo_valor_atual
    document.getElementById("valor_oferta").innerText = f"{soma}"

    valor_oferta_cal = document.getElementsByClassName("valor_oferta")[0].textContent
    valor_numerico = float(valor_oferta_cal.replace(/[^\d,]/g, '').replace(',', '.'))
    document.getElementById("valor_oferta").value = valor_numerico

    calcular()

    adicionar_linha_maior_oferta()


def enviar_lance(event):
    valor_lance = document.getElementById("valor_lance").value
    valor_atual = document.getElementById("valor_oferta").innerText
    novo_valor_atual = valor_atual.replace(/[^\d,-]/g, "")

    novo_valor_lance = valor_lance.replace(/[^\d,-]/g, "")

    novo_valor_atual = float(novo_valor_atual)
    novo_valor_lance = float(novo_valor_lance)
    diferenca = novo_valor_lance - novo_valor_atual

    soma = diferenca + novo_valor_atual
    document.getElementById("valor_oferta").innerText = f"{soma}"

    valor_oferta_cal = document.getElementsByClassName("valor_oferta")[0].textContent
    valor_numerico = float(valor_oferta_cal.replace(/[^\d,]/g, '').replace(',', '.'))
    document.getElementById("valor_oferta").value = valor_numerico

    calcular()

    document.getElementById("valor_lance").value = ""

    tabela_lances = document.getElementById("lista_lances").getElementsByTagName("tbody")[0]
    maior_oferta = document.getElementById("valor_oferta").innerText

    nova_linha = "<tr>"
    nova_linha += f"<td><a href='#' rel='61560' class='excluir_lance'>Excluir</a></td>"
    nova_linha += "<td>Presencial</td>"
    nova_linha += "<td></td>"
    nova with cutoff of 65536 characters
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/atualizarmaiorlance", methods=["GET"])
def atualizarmaiorlance():
    valor = request.args.get("valor")
    
    # Código para atualizar o maior lance com o valor fornecido

    return jsonify({"success": True})


if __name__ == "__calculator__":
    app.run()
