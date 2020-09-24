# Generated by Django 3.1 on 2020-09-21 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcomments',
            options={'verbose_name': 'Комментарий поста', 'verbose_name_plural': 'Комментарии поста'},
        ),
        migrations.AlterModelOptions(
            name='postimages',
            options={'verbose_name': 'Картинка поста', 'verbose_name_plural': 'Картинки поста'},
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_postimages', to='blog.PostImages', verbose_name='Картинки блога'),
        ),
        migrations.AlterField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_post', to='blog.post', verbose_name='Пост в который нужно добавить эту картинку'),
        ),
    ]