# Generated by Django 3.2.25 on 2024-12-04 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('X', '0006_persona_telefono_suplente'),
    ]

    operations = [
        migrations.AddField(
            model_name='animales',
            name='datos',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='animales',
            name='diagnostico',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='animales',
            name='raza',
            field=models.CharField(default='', max_length=50),
        ),
    ]
