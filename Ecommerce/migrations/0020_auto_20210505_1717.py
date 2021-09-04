# Generated by Django 3.2 on 2021-05-05 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0019_auto_20210505_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='cart',
            new_name='Cart',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='user',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='Wish_List',
            field=models.JSONField(blank=True, default=''),
            preserve_default=False,
        ),
    ]