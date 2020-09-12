# Generated by Django 3.0.7 on 2020-09-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0021_tipper_char_fe'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='char_fe',
            field=models.IntegerField(blank=True, default=None, verbose_name='Железо'),
        ),
        migrations.AddField(
            model_name='stock',
            name='char_si',
            field=models.IntegerField(blank=True, default=None, verbose_name='Диоксид кремния'),
        ),
        migrations.AddField(
            model_name='tipper',
            name='char_si',
            field=models.IntegerField(blank=True, default=None, verbose_name='Диоксид кремния'),
        ),
    ]
