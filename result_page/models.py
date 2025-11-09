from django.db import models

# Create your models here.
from django.db import models

class MedicineInfo(models.Model):
    제품코드 = models.CharField(max_length=50, primary_key=True)  # Primary Key
    제품명 = models.CharField(max_length=255, null=True, blank=True)
    성분정보 = models.TextField(null=True, blank=True)
    효능효과 = models.TextField(null=True, blank=True)
    용법용량 = models.TextField(null=True, blank=True)
    저장방법 = models.TextField(null=True, blank=True)
    사용기간 = models.CharField(max_length=255, null=True, blank=True)
    사용상의주의사항 = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'medicine_info'  # 기존 테이블 이름 사용


class PastHistory(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # 사용자 ID
    제품명 = models.CharField(max_length=255, null=True, blank=True)
    제품코드 = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    Date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'past_history'  # 기존 테이블 이름
