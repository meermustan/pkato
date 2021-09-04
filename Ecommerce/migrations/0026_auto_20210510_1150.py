# Generated by Django 3.2 on 2021-05-10 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0025_auto_20210509_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=255, unique=True)),
                ('photo', models.ImageField(blank=True, upload_to='media/')),
            ],
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='Picture',
        ),
    ]