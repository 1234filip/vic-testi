# Generated by Django 3.1.3 on 2020-11-29 18:23

from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20201123_1514'),
    ]

    operations = [
        TrigramExtension()
    ]