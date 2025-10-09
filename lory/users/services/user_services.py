from django.shortcuts import get_object_or_404
from users.models import User

def sign_up(validated_data) -> tuple[bool, User | None, str | None]:

    try:
        # 이메일 중복 확인
        if User.objects.filter(email=validated_data.get("email")).exists():
            return False, None, "이미 존재하는 이메일입니다."
        
        user = User.objects.create_user(**validated_data)

        return True, user, None 
    except Exception as e:
        return False, None, str(e)
