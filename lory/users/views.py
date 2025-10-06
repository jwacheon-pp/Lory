from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets

def ping(request):
    return HttpResponse("users service \"PONG\"")

class UserViewSet(viewsets.ModelViewSet):
