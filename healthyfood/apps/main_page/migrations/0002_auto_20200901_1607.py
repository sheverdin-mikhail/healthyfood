# Generated by Django 3.1 on 2020-09-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headerslider',
            options={'managed': True, 'verbose_name': 'Слайд хедера', 'verbose_name_plural': 'Слайды хедера'},
        ),
        migrations.AddField(
            model_name='headerslider',
            name='slider_header',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Обозначение о чем этот слайд'),
        ),
        migrations.AlterModelTable(
            name='headerslider',
            table='',
        ),
    ]
