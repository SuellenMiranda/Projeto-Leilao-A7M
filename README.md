# Projeto-Leilao-A7M
Gestão de Projetos 
<br>
Um projeto de api para site que calcula o valor que vai receber em cima da porcentagem.
<br>



<br>

# Links

[PLANILHA BASE PARA PROJETO_ALUNO EDIÇÃO ONLINE](https://docs.google.com/spreadsheets/d/1gI2Gk0-D_KltLVE2XS8wdqqOF7CqgYjSPBmQ24J_ESQ/edit?usp=sharing)
<br>
[PLANILHA BASE PARA PROJETO_ALUNO BAIXAR](https://docs.google.com/spreadsheets/d/1XEvBLwEDWD4G38DiWBr-RY4JdXp5XNr5/edit?usp=share_link&ouid=106682525505356259672&rtpof=true&sd=true)
<br>
[Link do site](https://suellenmiranda.github.io/Projeto-Leilao-A7M/)

---

# Exemplo 1

Primeiro, vamos precisar da biblioteca Flask, que é um framework web para Python. Para instalá-lo, você pode usar o pip:

bash
Copy code
pip install Flask
Em seguida, vamos criar um arquivo app.py com o seguinte código:

python
Copy code
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
Este código cria uma rota /porcentagem que recebe dois parâmetros pela query string: valor e porcentagem. Ele calcula o valor da porcentagem ganho em cima do valor informado e retorna o resultado como um objeto JSON.

Para executar a aplicação, basta rodar o seguinte comando no terminal:

bash
Copy code
python app.py
Agora, você pode fazer uma requisição para a rota http://localhost:5000/porcentagem passando os parâmetros valor e porcentagem na URL. Por exemplo:

bash
Copy code
http://localhost:5000/porcentagem?valor=100&porcentagem=10
Esta requisição retorna o seguinte objeto JSON:

json
Copy code
{
  "resultado": 10.0
}
Isso significa que um ganho de 10% em cima de um valor de 100 é igual a 10.

como implemento isso em um site
Para implementar essa API em um site, você pode utilizar JavaScript para fazer uma requisição HTTP para o servidor que hospeda a API e, em seguida, exibir o resultado retornado pela API na página web.

Vou mostrar um exemplo básico de como fazer isso. Primeiro, adicione o seguinte código HTML à sua página:

html
Copy code
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
Este código cria um formulário com dois campos de entrada para o valor e a porcentagem. Quando o botão "Calcular" é clicado, ele chama a função calcularPorcentagem, que faz uma requisição HTTP para a API usando a função fetch. Quando a resposta da API é recebida, o resultado é exibido na página usando o elemento <p> com o ID resultado.

Para este exemplo funcionar, você precisa rodar o servidor que hospeda a API (no caso, o Flask) na mesma máquina e na mesma porta usada na URL da requisição (no caso, http://localhost:5000/porcentagem). Se o servidor estiver em outra máquina ou porta, você precisa ajustar a URL da requisição de acordo.




para testes de programação
tem como fazer essa api em outra linguagem?
Sim, é possível implementar essa API em outras linguagens além do Python. Eu vou lhe mostrar como implementar essa mesma funcionalidade em duas outras linguagens populares: JavaScript e PHP.

Implementação em JavaScript (Node.js)
Para criar essa API em JavaScript, usaremos o Node.js e o framework Express. Primeiro, instale o Node.js e o NPM (Node Package Manager) em seu sistema, e em seguida, crie um novo diretório e abra um terminal dentro dele.

Em seguida, execute o comando a seguir para inicializar um novo projeto Node.js e criar um arquivo package.json:

bash
Copy code
npm init -y
Em seguida, instale o Express digitando no terminal:

bash
Copy code
npm install express
Crie um arquivo chamado app.js com o seguinte código:

javascript
Copy code
const express = require('express')
const app = express()
const port = 3000

app.get('/porcentagem', (req, res) => {
  const valor = parseFloat(req.query.valor)
  const porcentagem = parseFloat(req.query.porcentagem)
  const resultado = valor * (porcentagem / 100)

  res.json({ resultado })
})

app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`)
})
Este código cria uma rota /porcentagem que recebe dois parâmetros pela query string: valor e porcentagem. Ele calcula o valor da porcentagem ganho em cima do valor informado e retorna o resultado como um objeto JSON.

Para executar o servidor, basta digitar no terminal:

bash
Copy code
node app.js
Agora, você pode fazer uma requisição para a rota http://localhost:3000/porcentagem passando os parâmetros valor e porcentagem na URL. Por exemplo:

bash
Copy code
http://localhost:3000/porcentagem?valor=100&porcentagem=10
Esta requisição retorna o seguinte objeto JSON:

json
Copy code
{
  "resultado": 10
}
Implementação em PHP
Para criar essa API em PHP, usaremos o framework Slim. Primeiro, certifique-se de que o PHP e o Composer (o gerenciador de pacotes do PHP) estejam instalados em seu sistema. Em seguida, crie um novo diretório e abra um terminal dentro dele.

Execute o seguinte comando para instalar o Slim:

bash
Copy code
composer require slim/slim "^4.0"
Em seguida, crie um arquivo chamado index.php com o seguinte código:

php
Copy code
<?php
use Slim\Factory\AppFactory;

require __DIR__ . '/vendor/autoload.php';

$app = AppFactory::create();
$app->addErrorMiddleware(true, true, true);

$app->get('/porcentagem', function ($request, $response, $args) {
  $valor = floatval($request->getQueryParam('valor'));
  $porcentagem = floatval($request->getQueryParam('porcentagem'));
  $resultado = $valor * ($porcentagem / 100);

  return $response->withJson(['resultado' => $resultado]);
});

$app->run();
Este código cria uma rota /porcentagem que recebe dois parâmetros pela query string: valor e porcentagem. Ele calcula o valor da porcentagem ganho em cima do valor informado e retorna o resultado como um objeto JSON.

Para executar o servidor

<br>
<br>
Atualizações <br>
[v] 3/7/2023 (excel online editado)
