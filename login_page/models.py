# login_page/models.py
from django.db import models

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=150, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.id
    class Meta:
        db_table = 'login_page'  # 원하는 테이블 이름으로 지정