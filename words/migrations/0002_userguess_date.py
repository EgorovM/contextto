# Generated by Django 4.1.3 on 2022-11-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userguess',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
