# Generated by Django 3.1.2 on 2020-11-29 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_auto_20201129_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinginfo',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.hotel'),
        ),
    ]
