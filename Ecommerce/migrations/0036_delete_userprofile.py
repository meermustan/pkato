# Generated by Django 3.2 on 2021-05-10 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0035_rename_profile_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
