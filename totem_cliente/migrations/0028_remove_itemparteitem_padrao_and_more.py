# Generated by Django 4.2.1 on 2023-05-14 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totem_cliente', '0027_rename_item_pai_itemparteitem_item_principal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemparteitem',
            name='padrao',
        ),
        migrations.RemoveField(
            model_name='produtoparteproduto',
            name='padrao',
        ),
        migrations.AlterField(
            model_name='produtoparteproduto',
            name='quantidade_maxima',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
