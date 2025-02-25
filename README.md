# Microservices Example

Este repositório contém um exemplo simples de arquitetura baseada em microserviços, composta por um backend em Python e um frontend com Nginx. O projeto está conteinerizado utilizando Docker e pode ser executado localmente com Docker Compose.

## Estrutura do Repositório

```
.
├── backend
│   ├── app.py           # Servidor HTTP simples em Python
│   └── Dockerfile       # Dockerfile para o backend
├── frontend
│   ├── index.html       # Interface do frontend
│   ├── default.conf     # Configuração do Nginx
│   └── Dockerfile       # Dockerfile para o frontend
├── docker-compose.yml   # Arquivo para orquestração dos containers
```

## Tecnologias Utilizadas

- **Docker** - Para conteinerização das aplicações.
- **Docker Compose** - Para orquestrar os containers.
- **Python (Backend)** - Servidor HTTP simples para fornecer uma API.
- **Nginx (Frontend)** - Servidor web para servir a interface e fazer proxy para o backend.

## Como Executar

### 1. Clonar o repositório
```sh
git clone https://github.com/seu-usuario/docker-microservice.git  
cd docker-microservice
```

### 2. Construir e subir os containers
```sh
docker compose up
```

O backend será iniciado na porta `5000` e o frontend na porta `80`.

### 3. Acessar a aplicação
Abra um navegador e acesse:
```
http://localhost
```

A aplicação frontend irá buscar dados da API backend e exibir a resposta na tela.

## API - Backend
O backend responde a requisições GET na rota `/api/data`. Exemplo de resposta JSON:

```json
{
    "message": "Oi do microservice Backend!",
    "info": "Aqui um exemplo simples de microservice."
}
```

## Configuração do Proxy no Nginx
O frontend está configurado para redirecionar as requisições para o backend utilizando o seguinte bloco no `default.conf`:

```nginx
location /api {
    proxy_pass http://backend:5000/api/data;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

Isso permite que o frontend consuma a API sem problemas de CORS.

## Encerrando os Containers
Para parar e remover os containers:
```sh
docker compose down
```

## Contribuição
Fique à vontade para abrir issues e enviar pull requests para melhorias! 😃

