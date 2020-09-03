# Generated by Django 3.1 on 2020-09-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0018_questionsanswers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageslider',
            name='anons_slider_bgcolor',
            field=models.CharField(default='#F0F0F0', max_length=7, verbose_name='Цвет фона слайда'),
        ),
        migrations.AlterField(
            model_name='questionsanswers',
            name='group',
            field=models.CharField(choices=[('weight', 'weight'), ('products', 'products'), ('tarifs', 'tarifs')], default='products', max_length=20, verbose_name='Группа вопросов'),
        ),
    ]