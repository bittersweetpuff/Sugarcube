# Generated by Django 2.2.6 on 2019-11-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='przelicznik',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
        ),
        migrations.AddField(
            model_name='meal',
            name='wrazliwosc',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
        ),
    ]
