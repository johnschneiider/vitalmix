# Generated by Django 5.1.2 on 2024-11-03 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
