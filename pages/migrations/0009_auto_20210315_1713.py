# Generated by Django 3.1.7 on 2021-03-15 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20210315_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stats',
            options={'ordering': ('querystring', 'amount'), 'verbose_name': 'Поисковый запрос', 'verbose_name_plural': 'Статистика поисковых запросов'},
        ),
    ]
