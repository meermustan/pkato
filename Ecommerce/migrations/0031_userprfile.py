# Generated by Django 3.2 on 2021-05-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0030_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPrfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=50)),
                ('Picture', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
