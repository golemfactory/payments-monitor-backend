# Generated by Django 3.2.12 on 2022-03-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220320_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
