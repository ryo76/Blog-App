# Generated by Django 5.0.1 on 2024-01-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='StyleSphere', max_length=255),
        ),
    ]
