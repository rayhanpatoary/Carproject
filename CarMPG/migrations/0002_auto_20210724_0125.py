# Generated by Django 2.2.13 on 2021-07-24 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarMPG', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
