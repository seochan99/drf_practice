from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer

# createAPIVIEW 사용 구현 
class RegisterView(generics.CreateAPIView): 
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.get_serializer(data = request.data)           # data 가져오기
        serializer.is_valid(raise_exception = True)                     # 검증 
        token = serializer.validated_data                               # validate()의 return값인 Token을 받아온다.
        return Response({"toekn":token.key}, status=status.HTTP_200_OK) # 반환