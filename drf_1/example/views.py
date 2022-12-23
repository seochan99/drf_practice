from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


@api_view(['GET'])
# request : POST GET imporamtion
def HelloAPI(request):
    return Response("hello world")
