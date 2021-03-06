# Generated by Django 2.2 on 2020-12-29 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriasUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.TextField(choices=[('SUPERVISOR', 'SUPERVISOR'), ('MAQUINISTA', 'MAQUINISTA'), ('1ER AYUDANTE', '1ER AYUDANTE'), ('2DO AYUDANTE', '2DO AYUDANTE'), ('3ER AYUDANTE', '3ER AYUDANTE')])),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'db_table': 'categoriaUsuario',
            },
        ),
        migrations.RemoveField(
            model_name='operario',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='parteimpresion',
            name='ayudante1ero',
            field=models.ForeignKey(db_column='ayudante1er', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ayudante1er', to='control.CategoriasUsuario', verbose_name='Primer ayudante'),
        ),
        migrations.AlterField(
            model_name='parteimpresion',
            name='ayudante2do',
            field=models.ForeignKey(db_column='ayudante2do', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ayudante2do', to='control.CategoriasUsuario', verbose_name='Segundo ayudante'),
        ),
        migrations.AlterField(
            model_name='parteimpresion',
            name='maquinista',
            field=models.ForeignKey(db_column='maquinista', on_delete=django.db.models.deletion.DO_NOTHING, related_name='maquinista', to='control.CategoriasUsuario', verbose_name='Maquinista'),
        ),
        migrations.AlterField(
            model_name='parteimpresion',
            name='supervisor',
            field=models.ForeignKey(db_column='supervisor', on_delete=django.db.models.deletion.DO_NOTHING, related_name='supervisor', to='control.CategoriasUsuario', verbose_name='Supervisor'),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Operario',
        ),
    ]
