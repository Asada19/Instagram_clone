# Generated by Django 3.1 on 2021-01-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210123_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stories',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
