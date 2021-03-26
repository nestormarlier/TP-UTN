# Generated by Django 2.2 on 2021-03-25 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenesproduccion',
            name='fecha_entrega',
        ),
        migrations.RemoveField(
            model_name='ordenesproduccion',
            name='fichaTecnica',
        ),
        migrations.RemoveField(
            model_name='ordenesproduccion',
            name='kg_prod',
        ),
        migrations.AddField(
            model_name='parteimpresion',
            name='ordenes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='control.OrdenesProduccion'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PedidoVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Fecha creación')),
                ('fecha_entrega', models.DateTimeField(verbose_name='Fecha de entrega')),
                ('kg_prod', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Kg. a producir')),
                ('fichaTecnica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.FichaTecnica')),
            ],
            options={
                'verbose_name': 'Pedido de Venta',
                'verbose_name_plural': 'Pedidos de Venta',
                'db_table': 'pedido_venta',
            },
        ),
        migrations.AddField(
            model_name='ordenesproduccion',
            name='pedido_venta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='control.PedidoVenta'),
            preserve_default=False,
        ),
    ]