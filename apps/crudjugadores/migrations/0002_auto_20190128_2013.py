# Generated by Django 2.1.4 on 2019-01-29 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudjugadores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]