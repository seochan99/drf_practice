from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .models import Profile

# createAPIVIEW 사용 구현 
class RegisterView(generics.CreateAPIView): 
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# 로그인 뷰
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.get_serializer(data = request.data)           # data 가져오기
        serializer.is_valid(raise_exception = True)                     # 검증 
        token = serializer.validated_data                               # validate()의 return값인 Token을 받아온다.
        return Response({"toekn":token.key}, status=status.HTTP_200_OK) # 반환

# 가져오는 기능, 수정 기능 필요
# 보는건 누구나, 수정은 해당 프로필의 주인만 
# permission_classes field 설정
class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer