import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Verifica se a URL solicitada é '/api/data'
        if self.path == '/api/data':
            # Cria um dicionário com a resposta
            data = {
                'message': 'Oi do microservice Backend!',
                'info': 'Aqui um exemplo de microservice.'
            }

            # Converte o dicionário em JSON
            json_data = json.dumps(data)

            # Define o tipo de conteúdo da resposta como JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Envia a resposta JSON
            self.wfile.write(json_data.encode('utf-8'))
        else:
            # Caso a URL solicitada não seja a '/api/data', retorna 404
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

# Função para rodar o servidor
def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('0.0.0.0', 5000)  # Define o host e a porta
    httpd = server_class(server_address, handler_class)
    print('Servidor rodando na porta 5000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
