# Generated by Django 3.0.7 on 2020-09-11 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0020_auto_20200911_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipper',
            name='char_fe',
            field=models.IntegerField(blank=True, default=None, verbose_name='Железо'),
        ),
    ]
