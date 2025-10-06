from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = User
        fields = [
            'url',
            'id',
            'email',
            'username',
            'name',
            'first_name',
            'last_name',
            'profile_image_url',
            'bio',
            'phone_number',
            'date_of_birth',
            'email_verified'
        ]
        extra_kwargs = {
            'url': {'view_name': 'users', 'lookup_field': 'id'},
            'users': {'lookup_field': 'username'}
        }