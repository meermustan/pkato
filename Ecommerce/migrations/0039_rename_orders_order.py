# Generated by Django 3.2 on 2021-05-11 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0038_orders_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
