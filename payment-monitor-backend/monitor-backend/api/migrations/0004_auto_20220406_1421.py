# Generated by Django 3.2.12 on 2022-04-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220406_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='invoice',
        ),
        migrations.AddField(
            model_name='agreement',
            name='amount_accepted',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AddField(
            model_name='agreement',
            name='amount_due',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AddField(
            model_name='agreement',
            name='amount_paid',
            field=models.CharField(default='0', max_length=64),
        ),
        migrations.AddField(
            model_name='agreement',
            name='amount_scheduled',
            field=models.CharField(default='0', max_length=64),
        ),
    ]