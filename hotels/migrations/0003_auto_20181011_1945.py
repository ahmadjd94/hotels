# Generated by Django 2.1.2 on 2018-10-11 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_auto_20181011_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
