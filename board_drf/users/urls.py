from django.urls import path
from .views import RegisterView

# as_view()
urlpatterns = [
    path('register/', RegisterView.as_view()),
]
