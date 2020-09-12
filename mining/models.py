from django.db import models
import math

class Tipper(models.Model):
    """Модель самосвала"""
    number = models.CharField("Бортовой номер",default=None,max_length=10)
    model = models.CharField("Модель",max_length=10)
    max_weight = models.IntegerField("Максимальная грузоподъемность",default=None)
    cur_weight = models.IntegerField("Текущий вес",default=None)
    coordinates = models.CharField("Координаты",max_length=10,blank=True,null=True)
    char_fe = models.IntegerField("Железо",blank=True,default=None)
    char_si = models.IntegerField("Диоксид кремния", blank=True, default=None)

    @property
    def overload(self):
        if self.cur_weight > self.max_weight:
            over = round((self.cur_weight *100 / self.max_weight -100),2)   #Расчет перегруза
            return over
        else: return '-'


    def __str__(self):
        return self.number

    class Meta:
        verbose_name= "Самосвал"
        verbose_name_plural = "Самосвалы"


class Stock(models.Model):
    """Модель склада"""
    name = models.CharField("Название склада",max_length=50)
    capacity_before = models.PositiveIntegerField("Объем склада до разгрузки",default=None)
    capacity_after = models.PositiveIntegerField("Объем склада после разгрузки", blank=True, null=True,default=None)
    capacity_show = models.PositiveIntegerField("До разгрузки", blank=True, null=True,default=None,editable=False)
    char_fe = models.IntegerField("Железо",blank=True,default=None)
    char_si = models.IntegerField("Диоксид кремния", blank=True, default=None)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "Склад"
        verbose_name_plural = "Склады"
