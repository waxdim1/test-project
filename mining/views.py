from django.shortcuts import render
from django.views.generic import ListView
from .models import Tipper, Stock
import datetime
from django.http import HttpResponse
from shapely.geometry import Polygon,Point
from .forms import Input
from .functions import point_in


def calcul(request):
    stock = Stock.objects.get(name="Склад")
    if request.method == "POST":
        form = Input(request.POST)
        if form.is_valid():
            coordinates = request.POST.getlist('coordinate')    #Получение списка координат
            for tip in Tipper.objects.all():
                point_in(coordinates,tip,stock)
    else:
        form = Input()
    tippers = Tipper.objects.all()
    context = {"tippers":tippers,"stock":stock}
    return render(request,'mining/tipper_list.html', context)