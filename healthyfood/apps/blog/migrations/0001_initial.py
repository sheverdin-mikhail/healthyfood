# Generated by Django 3.1 on 2020-09-27 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя автора(необязательно)')),
                ('post_name', models.CharField(max_length=255, verbose_name='Заголовок поста')),
                ('post_text', models.TextField(blank=True, null=True, verbose_name='Содержимое поста')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пост',
            },
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=255, verbose_name='Название картинки')),
                ('post_img', models.ImageField(upload_to='blog_images', verbose_name='Картинки блога')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_post', to='blog.post', verbose_name='Пост в который нужно добавить эту картинку')),
            ],
            options={
                'verbose_name': 'Картинка поста',
                'verbose_name_plural': 'Картинки поста',
            },
        ),
        migrations.CreateModel(
            name='PostComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Текст комментария')),
                ('create_date', models.DateField(auto_now=True, verbose_name='Дата комментирования')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя автора')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Комментируемый пост')),
            ],
            options={
                'verbose_name': 'Комментарий поста',
                'verbose_name_plural': 'Комментарии поста',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_postimages', to='blog.PostImages', verbose_name='Картинки блога'),
        ),
    ]
