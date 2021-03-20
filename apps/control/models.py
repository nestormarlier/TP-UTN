from django.db import models
from datetime import datetime
import datetime

from django.contrib.auth.models import User
from apps.user.models import User
from django.forms import model_to_dict


class FichaTecnica(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(
        verbose_name='Ficha Técnica Activo', default=True)

    created = models.DateTimeField(
        verbose_name='Fecha de alta', auto_now_add=True, db_column='creado')
    modified = models.DateTimeField(
        verbose_name='Fecha modificado', auto_now=True, db_column='modificado')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # EN NULO SI SIGUE ACTIVO
    delete = models.DateField(verbose_name='Fecha baja', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Ficha Técnica'
        verbose_name_plural = 'Fichas Técnicas'
        db_table = 'ficha_tecnica'
        ordering = ['id']

    def  toJSON(self):
        item = model_to_dict(self)
        return item

class Impresora(models.Model):
    impresora_id = models.IntegerField(primary_key=True, verbose_name='Número')
    nombre = models.CharField(max_length=30, unique= True)

    created = models.DateTimeField(
        verbose_name='Fecha de alta', auto_now_add=True, db_column='creado')
    modified = models.DateTimeField(
        verbose_name='Fecha modificado', auto_now=True, db_column='modificado')

    activo = models.BooleanField(verbose_name='Impresora Activa', default=True)
    # EN NULO SI SIGUE ACTIVO

    def __str__(self):
        return "%s" % self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'impresora'
        ordering = ['impresora_id']

class Parada(models.Model):
    NOMBRE_CHOICES = [
        ('TINTAS', 'TINTAS'),
        ('MONTAJE', 'MONTAJE'),
        ('DEPÓSITO', 'DEPÓSITO'),
        ('MANTENIMIENTO', 'MANTENIMIENTO'),
        ('PROGRAMACIÓN', 'PROGRAMACIÓN'),
        ('SUPERVICIÓN', 'SUPERVICIÓN'),
        ('PRODUCCIÓN', 'PRODUCCIÓN'),
        ('OPERATIVO', 'OPERATIVO'),
        ('CALIDAD', 'CALIDAD')
    ]
    #parada_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, unique=True)

    created = models.DateTimeField(
        verbose_name='Fecha de alta', auto_now_add=True, db_column='creado')
    modified = models.DateTimeField(
        verbose_name='Fecha modificado', auto_now=True, db_column='modificado')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    active = models.BooleanField(
        verbose_name='Ficha Técnica Activo', default=True)
    sector_asignado = models.CharField(max_length=30, choices=NOMBRE_CHOICES)
    # EN NULO SI SIGUE ACTIVO
    delete = models.DateField(verbose_name='Fecha baja', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'parada'
        ordering = ['id']

    def toJSON(self):
        item = model_to_dict(self)
        return item

class CambioMecanico(models.Model):
    #cambio_id = models.AutoField(primary_key=True)
    create = models.DateTimeField(
        verbose_name='Fecha creación', null=True, blank=True, default=datetime.datetime.now)
    modified = models.DateTimeField(
        verbose_name='Fecha modificado', auto_now=True, db_column='modificado')
    parada = models.ForeignKey(
        Parada, verbose_name='Parada', on_delete=models.CASCADE, null=True, blank=True)
    fecha_fin = models.DateTimeField(verbose_name='Fin cambio')

    class Meta:
        verbose_name = 'Cambio mecánico'
        verbose_name_plural = 'Cambios Mecánicos'
        db_table = 'cambio_mecanico'

    def __str__(self):
        return str(self.parada)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Setup(models.Model):
    create = models.DateTimeField(
        verbose_name='Fecha creación', null=True, blank=True, default=datetime.datetime.now)
    parada = models.ForeignKey(
        Parada, verbose_name='Parada', on_delete=models.CASCADE, null=True, blank=True)
    fecha_fin = models.DateTimeField(verbose_name='Fin Setup')

    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setups'
        db_table = 'setup'

    def __str__(self):
        return str(self.parada)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Produccion(models.Model):
    #produccion_id = models.AutoField(primary_key=True)
    create = models.DateTimeField(
        verbose_name='Fecha de creación', null=True, blank=True, default=datetime.datetime.now)
    parada = models.ForeignKey(
        Parada, verbose_name='Parada', on_delete=models.CASCADE, null=True, blank=True)
    fecha_fin = models.DateTimeField(verbose_name='Fin producción')

    class Meta:
        verbose_name = 'Producción'
        verbose_name_plural = 'Producciones'
        db_table = 'produccion'

    def __str__(self):
        return str(self.parada)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class ObservacionesGles(models.Model):
        #produccion_id = models.AutoField(primary_key=True)
    create = models.DateTimeField(
        verbose_name='Fecha de creación', null=True, blank=True, default=datetime.datetime.now)
    observacion = models.TextField(verbose_name='Observaciones generales', null=True, blank=True)
    fecha_fin = models.DateTimeField(verbose_name='Fin observación')

    class Meta:
        verbose_name = 'Observación general'
        verbose_name_plural = 'Observaciones generales'
        db_table = 'observaciones_gles'

    def __str__(self):
        return str(self.observacion)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class ObsMantenimiento(models.Model):
    #produccion_id = models.AutoField(primary_key=True)
    mecanico = models.ForeignKey(User, verbose_name='Mecánico', on_delete=models.DO_NOTHING, related_name='mecanico', db_column='mecanico')
    create = models.DateTimeField(
        verbose_name='Fecha de creación', null=True, blank=True, default=datetime.datetime.now)
    observacion = models.TextField(verbose_name='Observaciones del mecánico', null=True, blank=True)

    class Meta:
        verbose_name = 'Observación mantenimiento'
        verbose_name_plural = 'Observaciones mantenimiento'
        db_table = 'observaciones_mant'

    def __str__(self):
        return str(self.observacion)

    def toJSON(self):
        item = model_to_dict(self)
        return item

class ParteImpresion(models.Model):
    #parte_id = models.AutoField(verbose_name='Orden impresión', primary_key=True)
    maquinista = models.ForeignKey(User, verbose_name='Maquinista', on_delete=models.DO_NOTHING,
                                   related_name='maquinista', db_column='maquinista')
    supervisor = models.ForeignKey(User, verbose_name='Supervisor', on_delete=models.DO_NOTHING,
                                   related_name='supervisor', db_column='supervisor')
    ayudante1ero = models.ForeignKey(User, verbose_name='Primer ayudante', on_delete=models.DO_NOTHING,
                                     related_name='ayudante1er', db_column='ayudante1er')
    ayudante2do = models.ForeignKey(User, verbose_name='Segundo ayudante', on_delete=models.DO_NOTHING,
                                    related_name='ayudante2do', db_column='ayudante2do')
    fichaTecnica = models.ForeignKey(FichaTecnica, on_delete=models.CASCADE)
    impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE)
    create = models.DateField(verbose_name='Fecha creación', auto_now_add=True)
    cambio = models.ManyToManyField(CambioMecanico, verbose_name="Cambio Mecánico", related_name='cambio',
                                    db_column='cambio_id', blank=True)
    setup = models.ManyToManyField(Setup, verbose_name='RM AC AP', related_name='setup', db_column='setup',
                                   blank=True)
    produccion = models.ManyToManyField(Produccion, verbose_name='Producción', related_name='produccion',
                                        db_column='produccion', blank=True)
    observacion_gral = models.ManyToManyField(ObservacionesGles, verbose_name = 'Observaciones generales', related_name= 'observacion_gral', db_column='obs_gles', blank=True)
    observacion_mant = models.ManyToManyField(ObsMantenimiento, verbose_name='Observaciones de mantenimiento', related_name='observacion_mant', db_column='obs_mant', blank=True)

    metros_registro = models.IntegerField(verbose_name='Metros registro')
    kg_registro = models.IntegerField(verbose_name='Kg. registro')
    metros = models.IntegerField(verbose_name='Metros producidos')
    kg = models.IntegerField(verbose_name='Kg producidos')

    class Meta:
        verbose_name = 'Parte de impresión'
        verbose_name_plural = 'Partes de impresión'
        db_table = 'parte_impresion'

    def __str__(self):
        return str(self.id)

    def toJSON(self):
        item = model_to_dict(self)

        # POST dicccionario con las paradas en los cambios
        item['cambio'] = [model_to_dict(c) for c in self.cambio.all()]

        # POST dicccionario con las paradas en los setups
        item['setup'] = [model_to_dict(s) for s in self.setup.all()]
        
        # POST dicccionario con las paradas en lo producción
        item['produccion'] = [model_to_dict(p) for p in self.produccion.all()]
        
        return item
