# Generated by Django 3.2 on 2021-05-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0012_remove_product_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Choices',
            field=models.JSONField(blank=True, default=''),
            preserve_default=False,
        ),
    ]