import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import PersonData
from django.utils import timezone

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import PersonData

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if self.user.is_anonymous:
            await self.close()
        else:
            # Example: Group name specific to redcross
            self.group_name = 'redcross'
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({
            'message': 'Received your message. This is an echo.'
        }))

    async def send_notification(self, event):
        notification_id = event['notification_id']
        try:
            notification = await sync_to_async(PersonData.objects.get)(pk=notification_id)
            await self.send(text_data=json.dumps({
                'message': f"Notification: {notification.Person_Name} - {notification.Component} is expiring on {notification.Expiry_Date}."
            }))
        except PersonData.DoesNotExist:
            pass
