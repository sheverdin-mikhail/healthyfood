# Generated by Django 3.1 on 2020-09-20 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0013_auto_20200920_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsanswers',
            name='group',
            field=models.CharField(choices=[('tarifs', 'Тарифы'), ('products', 'Продукты'), ('weight', 'Вес')], default='products', max_length=20, verbose_name='Группа вопросов'),
        ),
    ]
