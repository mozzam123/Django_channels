from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = "client1"
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name     
            )
        self.accept()
        print('Accepted')
        # self.send()
        


    def receive(self):
        async_to_sync(self.channel_layer.group_send)(
            "client1",
            {
                "type": "chat.message",
                "text": "Mozzam",
            },
        )
       

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("client1", self.channel_name)

    def group_message(self, event):
        self.send(text_data=event["text"])
        