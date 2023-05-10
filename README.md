# Projeto-Leilao-A7M
Este é um projeto de API para um site que calcula o valor a receber com base em uma porcentagem. A aplicação é desenvolvida em Python com o framework Flask.

## Começando
Para obter uma cópia deste projeto em sua máquina local, você pode fazer o download ou clonar o repositório do GitHub.

## Pré-requisitos
Antes de prosseguir com a instalação, certifique-se de ter o seguinte software instalado em sua máquina:

* Python
* Flask

## Exemplo de código
Aqui está um exemplo de como instalar as dependências do projeto usando o pip:

```
pip install -r requirements.txt
Instalação
Para instalar o projeto, basta clonar o repositório e executar o seguinte comando:
```

```
python app.py
A API estará disponível no endereço http://localhost:5000.
```

## Como funciona
A API utiliza uma função para obter o valor atual do leilão e, em seguida, calcula o valor correspondente a 5% desse valor. A rota '/leilao' retorna os dois valores em formato JSON.

```python

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

## Testes
Para testar a API, é possível utilizar o código fonte de uma parte necessária e testar a aplicação em funcionamento. Para isso, você pode acessar o servidor privado através do link abaixo, substituindo o {ip} pelo IP atual:

```
http://{ip}:5500/index.html
```
Certifique-se de que a aplicação esteja rodando ao vivo com o VS Code para que seja possível testar a API. É importante destacar que não é necessário implementar uma segurança muito reforçada para o projeto, já que se trata de algo específico para o leiloeiro.

Executando os testes
Para executar os testes automatizados do projeto, você pode usar o pytest. Basta executar o seguinte comando na raiz do projeto:

```
pytest
```

## Atualizações 
data: mm/dd/yyyy

- [x] 2/15/2023 (Reunião para grupo montado)
- [x] 2/22/2023 (Reunião para a criação de tudo)
- [x] 3/1/2023 (Reunião para excel editado pela 1ª vez)
- [ ] 3/2/2023 (Reunião para reuniao marcada - não aconteceu)
- [x] 3/7/2023 (Reunião para excel online editado)
- [x] 3/9/2023 (Reunião para excel)
- [x] 3/15/2023 (proxima reuniao - proxima aula)
- [x] 5/02/2023 (Reunião sobre a implementação apó criação da base da api)
- [x] 5/09/2023 (Reunião sobre os erros que estão acontecendo)

## Contribuidores
* Davi Amaral
* Daniel Colodete
* Luiz Guilherme
* Samuel Moacyr
* Suellen Miranda

## Licença
Este projeto é Privado.

## Agradecimentos
Gostaríamos de agradecer a todos que ajudaram no desenvolvimento deste projeto.

