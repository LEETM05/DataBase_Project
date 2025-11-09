from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, id, password=None, **extra_fields):
        if not id:
            raise ValueError('아이디는 필수입니다.')
        user = self.model(id=id, **extra_fields)
        user.set_password(password)  # 비밀번호 해싱
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('관리자는 is_staff=True 여야 합니다.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('관리자는 is_superuser=True 여야 합니다.')

        return self.create_user(id, password, **extra_fields)

class User(AbstractBaseUser):
    id = models.CharField(primary_key=True, max_length=150, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)  # Django 인증 시스템 요구 필드

    objects = CustomUserManager()

    USERNAME_FIELD = 'id'  # 로그인 시 사용할 필드
    REQUIRED_FIELDS = []  # 추가로 입력받을 필드 (예: 이메일 등)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'user_table'  # MySQL 테이블 이름