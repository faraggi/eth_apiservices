# Generated by Django 2.0.8 on 2018-09-08 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180908_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='block_hash',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]