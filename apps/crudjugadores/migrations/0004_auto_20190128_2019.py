# Generated by Django 2.1.4 on 2019-01-29 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudjugadores', '0003_auto_20190128_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]