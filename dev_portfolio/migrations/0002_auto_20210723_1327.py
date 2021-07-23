# Generated by Django 3.1.2 on 2021-07-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='developer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]