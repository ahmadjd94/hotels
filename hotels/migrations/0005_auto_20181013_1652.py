# Generated by Django 2.1.2 on 2018-10-13 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_auto_20181013_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='hotels.Hotel'),
        ),
    ]
