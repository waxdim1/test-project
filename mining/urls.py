from django.urls import path
from . import views

urlpatterns = [

    path('check/', views.calcul, name='calc'),

]
