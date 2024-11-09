# myapp/consumers.py

import json
from channels.generic.websocket import WebsocketConsumer

class MyWebSocketConsumer(WebsocketConsumer):
    def connect(self):
        # Aceitar a conexão WebSocket
        self.accept()

    def disconnect(self, close_code):
        # Desconectar o WebSocket
        pass

    def receive(self, text_data):
        # Receber mensagem do cliente (texto JSON)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Enviar mensagem de volta para o cliente
        self.send(text_data=json.dumps({
            'message': message
        }))
