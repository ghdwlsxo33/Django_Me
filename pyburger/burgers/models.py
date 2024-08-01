from django.db import models

# Create your models here.
# 실제로 데이터 베이스에 반영이 되는 클래스
# 스프링에서 엔티티 클래스와 동일
# 클래스를 정의 하면 자동으로 테이블을 생성해준다 ORM

#python manage.py makemigrations burgers
# #python manage.py migrate burgers




class Burger(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)