# Projeto-Leilao-A7M
Gestão de Projetos 
<br>
Um projeto de api para site que calcula o valor que vai receber em cima com porcentagem.
<br>
<br>


<br>

---

### Exemplo 1 (PYTHON)

Primeiro, vamos precisar da biblioteca Flask, que é um framework web para Python. Para instalá-lo, você pode usar o pip:

```bash
bash
pip install Flask

```

Em seguida, vamos criar um arquivo **`app.py`** com o seguinte código:

```python

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/porcentagem')
def porcentagem():
    valor = float(request.args.get('valor'))
    porcentagem = float(request.args.get('porcentagem'))
    resultado = valor * (porcentagem/100)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run()

```

Este código cria uma rota **`/porcentagem`** que recebe dois parâmetros pela query string: **`valor`** e **`porcentagem`**. Ele calcula o valor da porcentagem ganho em cima do valor informado e retorna o resultado como um objeto JSON.

Para executar a aplicação, basta rodar o seguinte comando no terminal:

```bash
bash
python app.py

```

Agora, você pode fazer uma requisição para a rota **`http://localhost:5000/porcentagem`** passando os parâmetros **`valor`** e **`porcentagem`** na URL. Por exemplo:

```bash
bash
http://localhost:5000/porcentagem?valor=100&porcentagem=10

```

Esta requisição retorna o seguinte objeto JSON:

```json
jsonCopy code
{
  "resultado": 10.0
}

```

Isso significa que um ganho de 10% em cima de um valor de 100 é igual a 10.

### Implementação

Para implementar essa API em um site, você pode utilizar JavaScript para fazer uma requisição HTTP para o servidor que hospeda a API e, em seguida, exibir o resultado retornado pela API na página web.

Vou mostrar um exemplo básico de como fazer isso. Primeiro, adicione o seguinte código HTML à sua página:

```html
html
<!DOCTYPE html>
<html>
<head>
  <title>Calculadora de Porcentagem</title>
</head>
<body>
  <h1>Calculadora de Porcentagem</h1>
  <form>
    <label for="valor">Valor:</label>
    <input type="text" id="valor"><br>

    <label for="porcentagem">Porcentagem:</label>
    <input type="text" id="porcentagem"><br>

    <button type="button" onclick="calcularPorcentagem()">Calcular</button>
  </form>

  <p id="resultado"></p>

  <script>
    function calcularPorcentagem() {
      const valor = document.getElementById('valor').value;
      const porcentagem = document.getElementById('porcentagem').value;

      // Fazer requisição HTTP para a API
      fetch(`http://localhost:5000/porcentagem?valor=${valor}&porcentagem=${porcentagem}`)
        .then(response => response.json())
        .then(data => {
          // Exibir resultado na página
          document.getElementById('resultado').textContent = `O ganho de ${porcentagem}% em cima de ${valor} é ${data.resultado}.`;
        })
        .catch(error => {
          console.error(error);
          document.getElementById('resultado').textContent = 'Ocorreu um erro ao calcular o ganho de porcentagem.';
        });
    }
  </script>
</body>
</html>

```

Este código cria um formulário com dois campos de entrada para o valor e a porcentagem. Quando o botão "Calcular" é clicado, ele chama a função **`calcularPorcentagem`**, que faz uma requisição HTTP para a API usando a função **`fetch`**. Quando a resposta da API é recebida, o resultado é exibido na página usando o elemento **`<p>`** com o ID **`resultado`**.

Para este exemplo funcionar, você precisa rodar o servidor que hospeda a API (no caso, o Flask) na mesma máquina e na mesma porta usada na URL da requisição (no caso, **`http://localhost:5000/porcentagem`**). Se o servidor estiver em outra máquina ou porta, você precisa ajustar a URL da requisição de acordo.



# Atualizações 

- [x] 2/15/2023 (Grupo montado)
- [x] 2/22/2023 (criação de tudo)
- [x] 3/1/2023 (excel editado pela 1ª vez)
- [ ] 3/2/2023 (reuniao marcada - não aconteceu)
- [x] 3/7/2023 (excel online editado)
- [x] 3/9/2023 (excel + reuniao)
- [ ] 3/15/2023 (proxima reuniao - proxima aula)



```python
flask
from flask import Flask, jsonify

app = Flask(__name__)

# Função para obter o valor atual do leilão
def get_valor_leilao():
    # Aqui você pode usar uma API ou web scraping para obter o valor atual do leilão
    valor_atual = 1000  # Exemplo: valor atual do leilão é 1000
    return valor_atual

# Rota para retornar o valor atual do leilão e o valor calculado de 5%
@app.route('/leilao')
def leilao():
    valor_atual = get_valor_leilao()
    valor_5_porcento = valor_atual * 0.05
    return jsonify({
        'valor_atual': valor_atual,
        'valor_5_porcento': valor_5_porcento
    })

if __name__ == '__main__':
    app.run()
```
