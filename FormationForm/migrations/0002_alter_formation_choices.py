# Generated by Django 4.0.6 on 2022-09-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormationForm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='choices',
            field=models.CharField(max_length=650, verbose_name='last_name'),
        ),
    ]
