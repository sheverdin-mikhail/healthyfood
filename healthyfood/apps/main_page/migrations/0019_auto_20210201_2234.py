# Generated by Django 3.1 on 2021-02-01 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0018_auto_20210201_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsanswers',
            name='group',
            field=models.CharField(choices=[('products', 'Продукты'), ('tarifs', 'Тарифы'), ('weight', 'Вес')], default='products', max_length=20, verbose_name='Группа вопросов'),
        ),
    ]