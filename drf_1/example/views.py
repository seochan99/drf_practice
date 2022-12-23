from rest_framework import viewsets, permissions, generics, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer

# def 
@api_view(['GET'])
# request : POST GET imporamtion
def HelloAPI(request):
    return Response("hello world")

@api_view(['GET','POST'])
def booksAPI(request):
    if request.method == 'GET':
        books = Book.objects.all() #책 모델 전체 데이터 가져오기
        serializer = BookSerializer(books,many=True) #시리얼라이저에 전체 데이터 한번에 넣기, 직렬화, 여러데이터 처리
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(): #유효한 데이터 
            serializer.save() #시리얼라이즈 역직렬화 통해 저장 
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def bookAPI(request,bid):
    book = get_object_or_404(Book,bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data,status=status.HTTP_200_OK)

# class
class BooksAPI(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUES)

class BookAPI(APIView):
    def get(self,request,bid):
        book = get_object_or_404(Book,bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)

# Mixins 
class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class BookAPIMixins(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)