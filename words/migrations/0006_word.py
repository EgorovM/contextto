# Generated by Django 4.1.3 on 2022-11-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_alter_usersession_session_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=128)),
            ],
        ),
    ]
