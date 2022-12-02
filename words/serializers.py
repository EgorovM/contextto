from rest_framework import serializers

from .models import UserSession


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ['session_id']
