# Generated by Django 3.2 on 2021-05-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0037_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Item',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
