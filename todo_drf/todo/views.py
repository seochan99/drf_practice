from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import *

# 투두들 
class TodosAPIView(APIView):
    # 가져오기
    def get(self,request):
        todos = Todo.objects.filter(complete=False)
        serializers = TodoSimpleSerializers(todos,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
# 게시 
    def post(self, request):
        serializers = TodoCreateSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

# 투두 세부 
class TodoAPIView(APIView):
    #가져오기 
    def get(self,request,pk):
        todo = get_object_or_404(Todo,id=pk)
        serializers = TodoDetailSerializer(todo)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        todo = get_object_or_404(Todo,id=pk)
        serializers = TodoDetailSerializer(todo,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class DoneTodosAPIView(APIView):
    def get(self,reuqest):
        dones = Todo.objects.filter(complete=True)
        serializers = TodoSimpleSerializers(dones,many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class DoneTodoView(APIView):
    def get(self,request,pk):
        done = get_object_or_404(Todo,id=pk)
        done.complete = True
        done.save()
        serializer = TodoDetailSerializer(done)
        return Response(status=status.HTTP_200_OK)