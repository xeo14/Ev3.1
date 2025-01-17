# Generated by Django 3.2.25 on 2024-11-26 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('X', '0003_alter_basquetbolista_altura_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=2)),
                ('tipo', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='fotos/')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='basquetbolista',
            name='manage',
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
        migrations.DeleteModel(
            name='Basquetbolista',
        ),
        migrations.DeleteModel(
            name='Manage',
        ),
        migrations.AddField(
            model_name='animales',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='X.persona'),
        ),
    ]
