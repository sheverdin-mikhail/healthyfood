# Generated by Django 3.1 on 2020-09-02 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0013_auto_20200902_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название блюда')),
                ('menu_discription', models.CharField(max_length=500, verbose_name='Описание блюда')),
                ('big_img', models.ImageField(upload_to='img', verbose_name='Картинка большого слайда')),
                ('small_img', models.ImageField(upload_to='img', verbose_name='Картинка маленького слайда')),
                ('kkal', models.CharField(max_length=20, verbose_name='Колличество калорий')),
                ('gramm', models.CharField(max_length=20, verbose_name='Колличество грамм')),
            ],
            options={
                'verbose_name': 'Слайд-меню',
                'verbose_name_plural': 'Слайды-меню',
            },
        ),
    ]