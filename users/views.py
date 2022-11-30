from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from .models import User
from django.http import HttpResponse
import json
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserViewSet(ModelViewSet):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = [
                "email",
                "skill",
                "pk",
                "first_name",
                "last_name",
            ]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


def loginfunc(request):
    if not request.POST:
        request.POST = json.loads(request.body)

    email = request.POST.get("email", None)
    password = request.POST.get("password", None)

    if email is None or password is None:
        return HttpResponse(
            '{"status":"error","message":"email or password is empty"}', status=401
        )

    print(email, password)
    user = authenticate(email=email, password=password)

    if user is None:
        return HttpResponse(
            '{"status":"error","message":"email or password is wrong"}', status=401
        )
    else:
        token, _ = Token.objects.get_or_create(user=user)
        return HttpResponse(
            '{"status":"success","token":"' + token.key + '"}', status=200
        )


def signupFunc(request):
    if not request.POST:
        request.POST = json.loads(request.body)

    email = request.POST.get("email", None)
    password = request.POST.get("password", None)
    skill = request.POST.get("skill", "")
    first_name = request.POST.get("first_name", "")
    last_name = request.POST.get("last_name", "")

    if email is None or password is None:
        return HttpResponse(
            '{"status": "error", "message": "email or password is empty"}',
            status=401,
        )

    elif User.objects.filter(email=email).exists():
        return HttpResponse(
            '{"status": "error", "message": "email already exists"}', status=400
        )
    else:

        user = User(
            email=email, first_name=first_name, last_name=last_name, skill=skill
        )
        user.set_password(password)
        user.save()
    return HttpResponse(
        '{"status": "success", "message": "signup success"}', status=200
    )
