from rest_framework import serializers
from shop.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('idx', 'userid', 'query', 'answer', 'intent')