# Generated by Django 2.2.1 on 2019-06-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fifteenBooks',
            field=models.BooleanField(default=False),
        ),
    ]
