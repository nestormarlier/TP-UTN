# Generated by Django 2.2 on 2021-03-26 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_auto_20210325_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoventa',
            name='kg_prod',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9, verbose_name='Kg. a producir'),
        ),
    ]
