# Generated by Django 4.2.4 on 2023-08-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contato_alter_cadastros_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto_cadastrados',
            name='foto',
            field=models.ImageField(blank=True, db_column='Foto', null=True, upload_to=''),
        ),
    ]