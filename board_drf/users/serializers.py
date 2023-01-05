# 회원가입시
from django.contrib.auth.models import User # user 모델 
from django.contrib.auth.password_validation import validate_password #기본패스워드 검증 도구
from rest_framework import serializers
from rest_framework.authtoken.models import Token # 토큰 모델 
from rest_framework.validators import UniqueValidator # 이메일 중복 방지 

# 로그인 기능
# 장고 기본 authenticate함수, 설정한 defailtAuthBackend TokenAuth 방식으로 유저 인증해줌 
from django.contrib.auth import authenticate

# profile model 확장
from .models import Profile

# 회원가입
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

# 로그인
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True, write_only = True)
    # write only를 통해서 클라이언트->서버 방향의 역직렬화 가능, 서버-> 클라이언트 방향의 직렬화는 불가능하다
    # 로그인이니깐 클라이언트에서 서버로 요청 보내야하니깐!

     # 로그인 일치 여부 확인
    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user) # 해당 유저의 토큰 가져오기 
            return token                         # 토큰 반환 
        raise serializers.ValidationError(
                {"error":"TOKEN FIELDS DIDINT MATCH."}
            )
        return data

class ProfileView(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("nickname","position","subjects","images")