# Generated by Django 3.2.13 on 2022-04-26 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['model']},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['username'], 'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
    ]