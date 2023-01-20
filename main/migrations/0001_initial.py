# Generated by Django 4.1.5 on 2023-01-20 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='media')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('rating', models.IntegerField(default=0, help_text='Указывать рейтинг в integer')),
                ('cuisine', models.CharField(max_length=50)),
                ('work_time', models.DateTimeField(blank=True)),
                ('address', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Рестораны',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Название')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='media', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('post_category', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('BRK', 'Завтрак'), ('LUN', 'Обед'), ('DIN', 'Ужин')], default='BRK', max_length=3, verbose_name='Тип')),
                ('title_of_restourant', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='restourant_name', to='main.restaurant')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_or', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_order', to='main.post')),
                ('users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказ',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('hist_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.CharField(default='', max_length=10000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'Истории',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post_categories', to='main.post')),
                ('cuisine', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rest_category', to='main.restaurant')),
            ],
        ),
    ]
