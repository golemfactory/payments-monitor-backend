# Generated by Django 3.2.12 on 2022-03-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='yagna_time_confirmed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='yagna_time_created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='yagna_time_last_action',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='yagna_time_sent',
            field=models.DateTimeField(null=True),
        ),
    ]
