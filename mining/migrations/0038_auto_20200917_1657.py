# Generated by Django 3.0.7 on 2020-09-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0037_auto_20200917_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipper',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='tipper',
            name='coor_x',
            field=models.FloatField(blank=True, null=True, verbose_name='X координата'),
        ),
        migrations.AddField(
            model_name='tipper',
            name='coor_y',
            field=models.FloatField(blank=True, null=True, verbose_name='Y координата'),
        ),
    ]
