# Generated by Django 4.1.3 on 2023-05-06 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_news_date_added_ratind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratind',
            name='Status',
            field=models.CharField(choices=[('Убитая дорога', 'Убитая дорога'), ('Локальный дефект', 'Локальный дефект'), ('Локальный дефект исправлен', 'Локальный дефект исправлен'), ('Дорога отремонтирована', 'Дорога отремонтирована'), ('Нарушения на дороге', 'Нарушения на дороге')], default='Убитая дорога', max_length=78, verbose_name='Статус'),
        ),
    ]
