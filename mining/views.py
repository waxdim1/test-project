from django.shortcuts import render
from django.views.generic import ListView
from .models import Tipper, Stock
import datetime
from django.http import HttpResponse
from shapely.geometry import Polygon,Point
from .forms import Input


def calcul(request):
    if request.method == "POST":
        form  = Input(request.POST)
        stock = Stock.objects.get(name="Склад")
        polygon = Polygon(((30, 10), (40, 40), (20, 40), (10, 20), (30, 10))) #Инициализация полигона
        if form.is_valid():
            coordinates = request.POST.getlist('coordinate')    #Получение списка координат
            for tip in Tipper.objects.all():
                cor = coordinates.pop(0).split()      #Берутся элементы по очереди и проверяются на попадание в полигон
                if cor:
                    tip.coordinates = Point(tuple([int(num) for num in cor]))   #Преобразование списка в Point
                    tip.save()
                    if tip.coordinates.intersects(polygon):  #Если точка попадает то пересчитываем характеристики склада
                        print(tip.coordinates.intersects(polygon))
                        print('fak')
                        stock_fe = stock.char_fe * stock.capacity_before / 100  #Сколько железа до разгрузки
                        tip_fe = tip.char_fe * tip.cur_weight / 100             #Сколько железа в самосвале
                        stock_fe += tip_fe                                      #На складе после разгрузки

                        stock_si = stock.char_si * stock.capacity_before / 100  #Сколько кремния до разгрузки
                        tip_si = tip.char_si * tip.cur_weight / 100             #Сколько кремния в самосвале
                        stock_si += tip_si                                      #На складе после разгрузки

                        stock.capacity_after = tip.cur_weight + stock.capacity_before
                        stock.capacity_show = stock.capacity_before                   #Расчет обьема до и после разгрузки
                        stock.capacity_before = stock.capacity_after

                        stock.char_fe = stock_fe * 100 / stock.capacity_after
                        stock.char_si = stock_si * 100 / stock.capacity_after   #Перевод в проценты
                        print( stock.capacity_after,stock_fe,stock_si,stock.char_fe)
                        stock.save()
    else:
        form = Input()
    tippers = Tipper.objects.all()
    stocks = Stock.objects.all()
    context = {"tippers":tippers,"stocks":stocks}
    return render(request,'mining/tipper_list.html', context)