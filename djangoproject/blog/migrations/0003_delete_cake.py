# Generated by Django 4.2.4 on 2023-08-21 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_cake_price_remove_cake_updated_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cake',
        ),
    ]
