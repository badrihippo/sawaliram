# Generated by Django 2.2.3 on 2020-02-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sawaliram_auth', '0018_auto_20200224_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
