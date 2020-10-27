# Generated by Django 3.1 on 2020-10-25 19:56

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
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=1024, verbose_name='Адрес')),
                ('status', models.CharField(choices=[('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('ready', 'Заказ готов'), ('completed', 'Заказ выполнен')], default='new', max_length=100, verbose_name='Статус заказа')),
                ('buying_type', models.CharField(choices=[('self', 'Самовывоз'), ('delivery', 'Доставка')], default='self', max_length=100, verbose_name='Тип заказа')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('adress', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('orders', models.ManyToManyField(related_name='related_customer', to='main_page.Buy', verbose_name='Заказы покупателя')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя покупателя')),
            ],
            options={
                'verbose_name': 'Покупатель ',
                'verbose_name_plural': 'Покупатели',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_name', models.CharField(max_length=20, verbose_name='День недели')),
            ],
            options={
                'verbose_name': 'День недели',
                'verbose_name_plural': 'Дни недели',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название блюда')),
                ('menu_discription', models.CharField(max_length=500, verbose_name='Описание блюда')),
                ('big_img', models.ImageField(upload_to='img', verbose_name='Картинка большого слайда')),
                ('small_img', models.ImageField(upload_to='img', verbose_name='Картинка маленького слайда')),
                ('kkal', models.CharField(max_length=20, verbose_name='Колличество калорий')),
                ('gramm', models.CharField(max_length=20, verbose_name='Колличество грамм')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена блюда')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Цена со скидкой, если есть')),
                ('days_list', models.ManyToManyField(related_name='days', to='main_page.Days', verbose_name='Дни недели')),
            ],
            options={
                'verbose_name': 'Блюдо ',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.CreateModel(
            name='HeaderSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_header', models.CharField(blank=True, max_length=50, null=True, verbose_name='Обозначение о чем этот слайд')),
                ('main_text', models.CharField(max_length=300, verbose_name='Главный текст слайдера')),
                ('small_text', models.CharField(blank=True, max_length=200, null=True, verbose_name='Маленький текст слайдера')),
                ('button', models.CharField(blank=True, max_length=50, null=True, verbose_name='Текст кнопки')),
            ],
            options={
                'verbose_name': 'Слайд хедера',
                'verbose_name_plural': 'Слайды хедера',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя категории')),
                ('gramm', models.CharField(max_length=20, verbose_name='Диапазон ккал')),
                ('slug', models.SlugField(verbose_name='Ссылка категории')),
            ],
            options={
                'verbose_name': 'Категория меню',
                'verbose_name_plural': 'Категории меню',
            },
        ),
        migrations.CreateModel(
            name='PageHeaders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anons_header', models.CharField(max_length=100, verbose_name='Заголовок анонса')),
                ('anons_header_bold', models.CharField(blank=True, max_length=50, null=True, verbose_name='Выделенный текст заголовка анонса')),
                ('calculator_header', models.CharField(max_length=100, verbose_name='Заголовок калькулятора')),
                ('menu_header', models.CharField(max_length=100, verbose_name='Заголовок меню')),
                ('menu_smalltext', models.CharField(max_length=200, verbose_name='маленький текст в меню')),
                ('buy_header', models.CharField(max_length=100, verbose_name="Заголовок 'Закажи сейчас' ")),
                ('reviews_header', models.CharField(max_length=100, verbose_name='Заголовок отзывов')),
                ('questions_header', models.CharField(max_length=100, verbose_name='Заголовок вопросов')),
            ],
            options={
                'verbose_name': 'Заголовоки страницы',
                'verbose_name_plural': 'Заголовки страницы',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PageSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anons_slider_name', models.CharField(max_length=50, verbose_name='Имя слайда')),
                ('anons_slider_text', models.CharField(max_length=50, verbose_name='Текст слайда')),
                ('anons_slider_image', models.ImageField(upload_to='img', verbose_name='Картинка слайда')),
                ('anons_slider_bgcolor', models.CharField(default='#F0F0F0', max_length=7, verbose_name='Цвет фона слайда')),
                ('anons_slider_link', models.CharField(default='#', max_length=200, verbose_name='Сылка слайда')),
            ],
            options={
                'verbose_name': 'Слайд анонса',
                'verbose_name_plural': 'Слайды анонса',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='QuestionsAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=1000, verbose_name='Ответ')),
                ('group', models.CharField(choices=[('products', 'Продукты'), ('tarifs', 'Тарифы'), ('weight', 'Вес')], default='products', max_length=20, verbose_name='Группа вопросов')),
            ],
            options={
                'verbose_name': 'Вопрос и ответ',
                'verbose_name_plural': 'Вопросы и ответы',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('age', models.CharField(max_length=10, verbose_name='Возраст')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('before_img', models.ImageField(upload_to='img', verbose_name='Фото "до"')),
                ('after_img', models.ImageField(upload_to='img', verbose_name='Фото "после"')),
                ('num', models.PositiveIntegerField(default=1, verbose_name='Номер отзыва')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.menucategory', verbose_name='Меню(к которому сделан отзыв)')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='ProgrammsSmall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название маленького блока')),
                ('small_img', models.FileField(upload_to='img', verbose_name='Картинка блока')),
                ('cat', models.IntegerField(verbose_name='Номер блока')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.menucategory', verbose_name='Категория меню привязываемая к этому блоку')),
            ],
            options={
                'verbose_name': 'Маленький блок ',
                'verbose_name_plural': 'Маленькие блоки',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProgrammsBig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_text', models.CharField(max_length=50, verbose_name='Название блока')),
                ('big_img', models.FileField(upload_to='img', verbose_name='Картинка блока')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.menucategory', verbose_name='Категория привязываемая к блоку')),
            ],
            options={
                'verbose_name': 'Большой блок ',
                'verbose_name_plural': 'Большие блоки',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Итоговая цена товара')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.customer', verbose_name='Заказчик')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.food', verbose_name='Имя продукта')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.menucategory', verbose_name='Категория меню')),
                ('menu_items', models.ManyToManyField(to='main_page.Food', verbose_name='Позиции меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.PositiveIntegerField(default=0, verbose_name='Колличество блюд')),
                ('final_price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая цена заказа')),
                ('in_order', models.BooleanField(default=False)),
                ('for_anonymous_user', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_page.customer', verbose_name='Заказчик')),
                ('products', models.ManyToManyField(blank=True, to='main_page.Order', verbose_name='Заказанные блюда')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины покупателей',
            },
        ),
        migrations.AddField(
            model_name='buy',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_page.cart', verbose_name='Корзина пользователя'),
        ),
        migrations.AddField(
            model_name='buy',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='main_page.customer', verbose_name='Заказчик'),
        ),
    ]
