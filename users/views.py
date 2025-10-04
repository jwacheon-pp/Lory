from django.http import HttpResponse

def ping(request):
    return HttpResponse("users service \"PONG\"")

def get_user(request):
    

    return HttpResponse("get_user response")
    