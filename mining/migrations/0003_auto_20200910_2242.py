# Generated by Django 3.0.7 on 2020-09-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0002_auto_20200910_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipper',
            name='overload',
        ),
        migrations.AlterField(
            model_name='stock',
            name='char_fe',
            field=models.PositiveIntegerField(blank=True, max_length=50, verbose_name='Железо'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='char_si',
            field=models.PositiveIntegerField(blank=True, max_length=50, verbose_name='Диоксид кремния'),
        ),
        migrations.AlterField(
            model_name='tipper',
            name='coordinates',
            field=models.IntegerField(blank=True, verbose_name='Координаты'),
        ),
        migrations.AlterField(
            model_name='tipper',
            name='cur_weight',
            field=models.IntegerField(default=None, verbose_name='Текущий вес'),
        ),
        migrations.AlterField(
            model_name='tipper',
            name='max_weight',
            field=models.IntegerField(default=None, verbose_name='Максимальная грузоподъемность'),
        ),
    ]
