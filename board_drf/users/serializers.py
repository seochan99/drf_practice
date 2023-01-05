from django.contrib.auth.models import User # user 모델 
from django.contrib.auth.password_validation import validate_password #기본패스워드 검증 도구
from rest_framework import serializers
from rest_framework.authtoken.models import Token # 토큰 모델 
from rest_framework.validators import UniqueValidator # 이메일 중복 방지 

class RegisterSerializer(serializers.ModelSerializer): #회원가입 시리얼 라이저
    # 이메일 
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())], #이메일 중복 검증 
    )
    # 비밀번호 1
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password], # 비밀번호 검증
    )

     # 비밀번호 중복 검사
    password2 = serializers.CharField(
        write_only = True,
        required = True
        )
    class Meta:
        model = User
        fields = ('username','password','password2','email')
    
    # 비밀번호 일치 여부 확인
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password":"PASSWORD FIELDS DIDINT MATCH."}
            )
        return data
    
    # CREATE 요청에 대한 create 메소드를 오버라이딩, 유저를 생성하고 토근 생성 과정 
    def create(self, validated_data):
        # 유저 만들기 
        user = User.objects.create_user(
            username=validated_data['username'], 
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])   # 비번 설정 
        user.save()                                     # 유저저장 
        token = Token.objects.create(user=user)         # 토큰 설정 
        return user