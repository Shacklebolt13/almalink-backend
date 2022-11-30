from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from .models import User


class UserViewSet(ModelViewSet):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ["email", "skill", "pk", "username", "first_name", "last_name"]

    queryset = User.objects.all()
    serializer_class = UserSerializer
