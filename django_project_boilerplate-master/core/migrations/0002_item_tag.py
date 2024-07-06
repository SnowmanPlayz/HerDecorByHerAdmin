# Generated by Django 4.2 on 2024-07-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tag',
            field=models.CharField(choices=[('N', 'New'), ('C', 'Candle'), ('F', 'Featured')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]