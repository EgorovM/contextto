# Generated by Django 4.1.3 on 2022-11-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0006_word'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailForNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=128)),
            ],
        ),
    ]
