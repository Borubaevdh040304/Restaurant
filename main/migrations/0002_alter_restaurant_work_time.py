# Generated by Django 4.1.5 on 2023-01-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='work_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
