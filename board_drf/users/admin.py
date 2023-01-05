from django.contrib import admin
# 유저모델과 프로필 모델이 하나인거처럼 통합하기
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    cdn_delete = False
    verbose_name_plural = "profile"

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

# 기존 유저어드민 등록 없애기 
admin.site.unregister(User)

# User, UserAdmin을 함께 등록하기 
admin.site.register(User,UserAdmin)