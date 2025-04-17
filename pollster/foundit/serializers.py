from rest_framework import serializers
from .models import Founditem, LostItem, User, FoundItemRequest


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']

class FoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founditem
        fields = '__all__'  # Convert all fields to JSON

class LostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        fields = '__all__'
        read_only_fields = ['user'] #This tells the API: "Hey, the user will be provided by the backend. Don’t expect it from the client."

class ItemRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundItemRequest
        fields = ['id', 'found_item', 'requester', 'status', 'created_at']
        read_only_fields = ['requester', 'created_at']
