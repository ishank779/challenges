from django.urls import path
from . import views
urlpatterns=[
    path("",views.index),
    path("<int:month>/",views.challenges_int ,name="month-challenge-int"),
    path("<str:month>/",views.challenges,name ="month-challenge"),
]