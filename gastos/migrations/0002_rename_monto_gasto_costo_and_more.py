# Generated by Django 5.1.2 on 2024-11-04 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gasto',
            old_name='monto',
            new_name='costo',
        ),
        migrations.RenameField(
            model_name='gasto',
            old_name='descripcion',
            new_name='nombre',
        ),
    ]
