# Generated by Django 3.2 on 2021-05-01 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ecommerce', '0002_delete_porduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Porduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('Description', models.TextField()),
                ('Category', models.CharField(max_length=150)),
                ('Sub_Category', models.CharField(max_length=150)),
                ('Brand', models.CharField(max_length=150)),
                ('Price', models.IntegerField()),
                ('Pub_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Questions', models.TextField(blank=True)),
            ],
        ),
    ]
