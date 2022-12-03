from rest_framework import serializers

from .models import UserSession, UserGuess


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ['session_id']


class GuessSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGuess
        exclude = ['session']

    def create(self, validated_data):
        return UserGuess.objects.create(**validated_data)
