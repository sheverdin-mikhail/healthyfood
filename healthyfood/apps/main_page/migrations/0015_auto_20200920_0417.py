# Generated by Django 3.1 on 2020-09-20 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0014_auto_20200920_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_page.cart', verbose_name='Корзина пользователя'),
        ),
    ]