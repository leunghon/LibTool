# Generated by Django 4.1.7 on 2023-03-15 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0007_alter_record_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='year',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
