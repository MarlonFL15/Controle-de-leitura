# Generated by Django 3.2.6 on 2021-11-05 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211104_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leitura',
            name='nota',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]