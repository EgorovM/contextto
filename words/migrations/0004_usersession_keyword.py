# Generated by Django 4.1.3 on 2022-11-18 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_remove_userguess_date_userguess_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='keyword',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='words.daykeyword'),
            preserve_default=False,
        ),
    ]
