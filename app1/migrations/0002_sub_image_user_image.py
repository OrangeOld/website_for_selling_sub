# Generated by Django 4.2.5 on 2023-10-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub',
            name='image',
            field=models.ImageField(blank=True, upload_to='templates'),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='templates'),
        ),
    ]
