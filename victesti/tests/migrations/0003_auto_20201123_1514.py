# Generated by Django 3.1.3 on 2020-11-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_testimage_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimage',
            name='file',
            field=models.URLField(),
        ),
    ]
