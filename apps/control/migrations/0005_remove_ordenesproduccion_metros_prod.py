# Generated by Django 2.2 on 2021-03-26 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_auto_20210325_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenesproduccion',
            name='metros_prod',
        ),
    ]