from rest_framework import serializers
from django.contrib.auth import get_user_model
from newsfeed_portal.apps.core.api.serializers import DynamicFieldsModelSerializer
from newsfeed_portal.apps.news import models as models_news


User = get_user_model()


class UserSerializer(DynamicFieldsModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "name", "username", "email", "password", "confirm_password"]

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        if password != confirm_password:
            raise serializers.ValidationError({"password": "Passwords don't match"})
        return data

    def create(self, validated_data):
        username = validated_data.get("username")
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        # creating initial News Settings with empty values
        models_news.NewsSettings.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        name = validated_data.get("name")
        email = validated_data.get("email")
        instance.name = name
        instance.email = email
        instance.save()
        return instance
