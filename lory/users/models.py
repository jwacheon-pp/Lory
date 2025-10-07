# apps/users/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # password hash 처리
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=128)  # AbstractBaseUser의 set_password() 사용
    nickname = models.CharField(unique=True, max_length=50)

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    profile_image_url = models.URLField(blank=True, default="")
    bio = models.TextField(blank=True, default="")
    phone_number = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    is_active = models.BooleanField(default=True)  
    is_staff = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    last_login = models.DateTimeField(default=timezone.now)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"  # 로그인 필드
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    class Meta:
        db_table = "User"
        ordering = ["-date_joined"]
