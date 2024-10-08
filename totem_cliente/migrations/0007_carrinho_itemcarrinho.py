# Generated by Django 4.2.1 on 2023-05-11 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('totem_cliente', '0006_remove_restaurante_imagem_restaurante_logo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totem_cliente.restaurante')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totem_cliente.carrinho')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='totem_cliente.produto')),
            ],
        ),
    ]
