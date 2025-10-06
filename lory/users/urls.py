from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ping
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet)

# retrive / list / create/ update / partial_update / destroy 이외의 매핑은 @action으로 view에서 작성
urlpatterns = [
    path('ping/', ping),
    path('', include(router.urls)),
]