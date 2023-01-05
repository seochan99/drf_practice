from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Profile model : 유저모델 확장을 위해
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)   #primary_key = pk로 설정하여 통합적 관리
    nickname = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    subjects = models.CharField(max_length=128)
    image = models.ImageField(upload_to='profile/',deafult='deafult.png')

# post_saved이벤트 발생시 프로필 생성 
# 직접 프로필 생성 코드 작성 하지 않아도 유저 생성 이벤트 감지해 프로필 자동생성 가능
@receiver(post_save, sender = User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)