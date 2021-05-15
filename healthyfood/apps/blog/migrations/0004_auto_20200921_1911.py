# Generated by Django 3.1 on 2020-09-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя автора(необязательно)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(blank=True, null=True, verbose_name='Содержимое поста'),
        ),
    ]
