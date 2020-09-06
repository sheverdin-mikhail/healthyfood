# Generated by Django 3.1 on 2020-09-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0024_auto_20200906_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='name',
            field=models.CharField(max_length=20, verbose_name='День недели'),
        ),
        migrations.AlterField(
            model_name='questionsanswers',
            name='group',
            field=models.CharField(choices=[('tarifs', 'Тарифы'), ('products', 'Продукты'), ('weight', 'Вес')], default='products', max_length=20, verbose_name='Группа вопросов'),
        ),
    ]
