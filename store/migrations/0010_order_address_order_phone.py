# Generated by Django 4.1.1 on 2022-10-26 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]