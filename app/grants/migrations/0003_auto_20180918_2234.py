# Generated by Django 2.1.1 on 2018-09-18 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0002_auto_20180918_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]