# Generated by Django 2.0.8 on 2018-09-08 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='gasUsedByTxn',
            new_name='gasusedbytx',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='timeStamp',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='TxHash',
            new_name='tx_hash',
        ),
    ]
