from shapely.geometry import Polygon,Point

def point_in(coordinates,tip,stock):
    stock.polygon = Polygon(((30, 10), (40, 40), (20, 40), (10, 20), (30, 10)))  # Инициализация полигона
    cor = coordinates.pop(0).split()
    if cor:
        tip.coor_x = float(cor[0])  #Сохранение координаты X
        tip.coor_y = float(cor[1])  #Сохранение координаты Y
        tup = tip.coor_x,tip.coor_y
        tip.save()
        point = Point(tup)  #Преобразование к кортежу и инициализация точки
        if point:
            if point.intersects(stock.polygon): #Если точка входит в полигон, то пересчитать значения
                calc_stock(tip, stock)

def calc_stock(tip,stock):
    stock_fe = ore(stock,tip,stock.char_fe,tip.char_fe)     #Посчитать железо на складе
    stock_si = ore(stock,tip, stock.char_si, tip.char_si)   #Посчитать кремний на складе

    stock.capacity_before = stock.capacity_after
    stock.capacity_after = tip.cur_weight + stock.capacity_before   #Расчет объемов до и после

    stock.char_fe = round(stock_fe * 100 / stock.capacity_after,1)      #Преобразование к процентам
    stock.char_si = round(stock_si * 100 / stock.capacity_after,1)
    stock.save()


def ore(stock,tip,st,ti):
    stock_ore = st * stock.capacity_after / 100
    tip_ore = ti * tip.cur_weight / 100             #Расчет количества руды
    stock_ore += tip_ore
    return stock_ore

