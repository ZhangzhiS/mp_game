# Generated by Django 3.2.7 on 2021-09-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0003_auto_20210920_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='level',
            field=models.IntegerField(default=1, help_text='用户等级'),
        ),
    ]
