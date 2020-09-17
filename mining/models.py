from django.db import models
import math

class Tipper(models.Model):
    """Модель самосвала"""
    number = models.CharField("Бортовой номер",default=None,max_length=10)
    model = models.CharField("Модель",max_length=10)
    max_weight = models.IntegerField("Максимальная грузоподъемность",default=None)
    cur_weight = models.IntegerField("Текущий вес",default=None)
    coor_x = models.FloatField("X координата",blank=True,null=True)
    coor_y = models.FloatField("Y координата",blank=True,null=True)
    char_fe = models.IntegerField("Железо",blank=True,default=None)
    char_si = models.IntegerField("Диоксид кремния", blank=True, default=None)

    @property
    def overload(self):
        if self.cur_weight > self.max_weight:
            over = round((self.cur_weight *100 / self.max_weight -100),2)   #Расчет перегруза
            return over
        else:
            return 0


    def __str__(self):
        return self.number

    class Meta:
        verbose_name= "Самосвал"
        verbose_name_plural = "Самосвалы"


class Stock(models.Model):
    """Модель склада"""
    name = models.CharField("Название склада",max_length=50)
    capacity_before = models.PositiveIntegerField("Объем склада до разгрузки",default=None)
    capacity_after = models.PositiveIntegerField("Объем склада после разгрузки",default=None)
    char_fe = models.FloatField("Железо")
    char_si = models.FloatField("Диоксид кремния")
    polygon = models.CharField("Координаты полигона", max_length=100,default=None,editable=False, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "Склад"
        verbose_name_plural = "Склады"
