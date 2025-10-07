from rest_framework import serializers
from users.models import User

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
        ]
        extra_kwargs = {
            'url': {'view_name': 'users-detail', 'lookup_field': 'id'},
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
