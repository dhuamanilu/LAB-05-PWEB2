# Generated by Django 4.0.5 on 2022-06-09 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_persona_donador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='donador',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(blank=True),
        ),
    ]