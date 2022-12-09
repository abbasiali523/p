from django.urls import path
from home.views import *
urlpatterns = [
    path('',home,name='home'),
    path('hello/',say_hello,name='hello'),
    path('detail/<int:todo_id>',views_detial,name='detail'),
]
