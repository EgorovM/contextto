# Generated by Django 4.1.3 on 2022-11-19 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_usersession_keyword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='session_id',
            field=models.CharField(db_index=True, max_length=30),
        ),
    ]