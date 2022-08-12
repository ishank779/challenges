from django.urls import path
from . import views
urlpatterns={
    path("<str:month>",views.challenges),
    path("<int:month>",views.challenges_int)
}