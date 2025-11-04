from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):

    username_field = 'email'

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id'] = user.id
        token['nickname'] = user.nickname
        token['email'] = user.email

        return token

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        # 사용자 인증 시도
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(_("Invalid email or password"))

        # SimpleJWT의 기본 validate 로직 실행 (토큰 생성 등)
        data = super().validate(attrs)
        data["user_id"] = self.user.id
        data["email"] = self.user.email

        return data

# User 정보 조회용 Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = User
        fields = [
            'url',
            'id',
            'email',
            'nickname',
            'password',
            'first_name',
            'last_name',
            'profile_image_url',
            'bio',
            'phone_number',
            'date_of_birth',
            'email_verified',
            'is_superuser',
            'is_staff',
        ]
        extra_kwargs = {
            'url': {'view_name': 'users-detail', 'lookup_field': 'pk'},
        }

# User 등록용 Serializer
class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = [
            'email',
            'nickname',
            'first_name',
            'last_name',
            'profile_image_url',
            'bio',
            'phone_number',
            'date_of_birth',
            'email_verified',
            'password',
        ]

class ModifyUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields =[
            'password',
            'nickname', 
            'bio', 
            'phone_number',
            'profile_image_url',
        ]