# Executando o Desafio com Docker Compose

Este é um exemplo simples de como executar a imagem `minha-api` usando o Docker Compose.

## Pré-requisitos

Certifique-se de ter o Docker e Docker Compose instalado em seu sistema. Para mais informações: <br>
https://docs.docker.com/get-docker/ <br>
https://docs.docker.com/compose/install/

## Passos

1. Clone o repositório do Desafio.

git clone https://github.com/diogoacavalcante/desafio_16052023

2. Navegue até o diretório clonado.

3. Execute o comando docker-compose up para iniciar a aplicaçãp, use o parâmetro -d para executar o comando em background.

docker-compose up <br>
docker-compose up -d

4. Acesse a aplicação:
Abra o seu navegador e acesse http://localhost:5000/. Você deverá ver a resposta da API contendo a hora atual e um número aleatório. Exemplo:

"Current Time: 2023-05-19 18:29:05 Random Number: 23"

5. Para parar a execução da aplicação, execute o comando "docker-compose down" dentro do diretório clonado.

-------------------------------------------------------------------

Path DockerHub https://hub.docker.com/r/diogoacavalcante/minha-api
