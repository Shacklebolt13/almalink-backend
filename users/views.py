from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import serializers
from .models import User
from rest_framework.response import Response
import json
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class UserViewSet(ReadOnlyModelViewSet):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ["email", "skill", "pk", "first_name", "last_name", "password"]

    queryset = User.objects.all()
    serializer_class = UserSerializer


def loginfunc(request):
    if not request.POST:
        request.POST = json.loads(request.body)

    email = request.POST.get("email", None)
    password = request.POST.get("password", None)

    if email is None or password is None:
        return Response(
            '{"status":"error","message":"email or password is empty"}', status=401
        )

    print(email, password)
    user = authenticate(email=email, password=password)

    if user is None:
        return Response(
            '{"status":"error","message":"email or password is wrong"}', status=401
        )
    else:
        token, _ = Token.objects.get_or_create(user=user)
        return Response('{"status":"success","token":"' + token.key + '"}', status=200)


def signupFunc(request):
    # request.POST = json.loads(request.body)
    if not request.POST:
        request.POST = json.loads(request.body)

    email = request.POST.get("username", None)
    password = request.POST.get("password", None)
    skill = request.POST.get("skill", None)

    if email is None or password is None:
        return Response(
            {"status": "error", "message": "username or password is empty"}, status=401
        )

    else:
        user = User(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
    return Response({"status": "success", "message": "signup success"}, status=200)
