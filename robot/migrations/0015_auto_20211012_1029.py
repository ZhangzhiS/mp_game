# Generated by Django 3.2.7 on 2021-10-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0014_auto_20211012_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mana_point',
            field=models.IntegerField(default=100, verbose_name='当前法力值'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='max_mana_point',
            field=models.IntegerField(default=100, verbose_name='最大法力值'),
        ),
    ]
