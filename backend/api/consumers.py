import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PhotoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("photo_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("photo_updates", self.channel_name)

    async def send_photo(self, event):
        await self.send(text_data=json.dumps({"photo_url": event["photo_url"]}))
