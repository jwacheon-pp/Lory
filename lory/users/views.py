from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.serializers import *
from users.models import User
from users.services import sign_up

def ping(request):
    return HttpResponse("users service \"PONG\"")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return SignUpSerializer
        if self.action == 'partial_update':
            return ModifyUserSerializer  
        return UserSerializer   

    def create(self, request, *args, **kwargs):

        # serializer에 넣고 검증
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        is_success, user, error = sign_up(serializer.validated_data)
        if not is_success:
            return Response({"detail": error}, status=status.HTTP_400_BAD_REQUEST)

        # 새로 생성된 user id 기반 URL 생성
        user_url = reverse('users-detail', args=[user.id], request=request)

        return Response(
            {"id": user.id, "url": user_url},
            status=status.HTTP_201_CREATED
        )

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer