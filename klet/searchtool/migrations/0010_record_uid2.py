# Generated by Django 4.1.7 on 2023-03-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0009_alter_record_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='uid2',
            field=models.CharField(default='Not Registered yet', max_length=100),
        ),
    ]
