from django.urls import path, include
from .views import *

urlpatterns = [
    path('hello/', HelloAPI),
    #fbv
    path('fbv/books/',booksAPI),
    path('fbv/book/<int:bid>/',bookAPI),
    # cbv 
    path("cbv/books/",BooksAPI.as_view()),
    path("cbv/book/<int:bid>/",BookAPI.as_view()),
    # mixin
    path("mixin/books/",BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>/",BookAPIMixins.as_view()),
    # 제네릭
    path("generic/books/",BooksAPIGenerics.as_view()),
    path("generic/book/<int:bid>/",BookAPIGenerics.as_view()),


]
