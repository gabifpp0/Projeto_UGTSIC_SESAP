# Generated by Django 5.1.5 on 2025-01-27 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroCV', '0005_alter_formulario_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='ip',
            field=models.GenericIPAddressField(default='0.0.0.0', unpack_ipv4=True),
        ),
    ]
