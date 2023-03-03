# Generated by Django 4.1.7 on 2023-02-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='telefono',
            field=models.IntegerField(verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.IntegerField(blank=True, verbose_name='Telefono'),
        ),
    ]
