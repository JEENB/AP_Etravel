# Generated by Django 3.1.2 on 2020-11-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_auto_20201129_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinginfo',
            name='hotel',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
