
from django.urls import path
from book.views import hello, check

urlpatterns = [
    path('add', hello),
    path('check/', check),


]