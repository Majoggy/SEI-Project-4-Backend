# Generated by Django 3.2.7 on 2021-09-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='user_Id',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
    ]
