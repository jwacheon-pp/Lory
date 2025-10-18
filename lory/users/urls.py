from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ping, EmailTokenObtainPairView
from django.urls import path, include

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

# retrive / list / create/ update / partial_update / destroy 이외의 매핑은 @action으로 view에서 작성
urlpatterns = [
    path('ping/', ping),
    path('', include(router.urls)),
    path('login/', EmailTokenObtainPairView.as_view(), name='login'),
]