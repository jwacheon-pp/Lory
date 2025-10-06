from django.http import HttpResponse
from rest_framework import viewsets
from users.serializers import UserSerializer
from users.models import User
from users.services import sign_up

def ping(request):
    return HttpResponse("users service \"PONG\"")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    