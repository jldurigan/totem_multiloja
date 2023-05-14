# Generated by Django 4.2.1 on 2023-05-14 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('totem_cliente', '0017_categoria_visivel'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='restaurante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='totem_cliente.restaurante'),
            preserve_default=False,
        ),
    ]
