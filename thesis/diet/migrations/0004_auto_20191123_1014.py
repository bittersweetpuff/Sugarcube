# Generated by Django 2.2.6 on 2019-11-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0003_meal_warning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='insulin_dose',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='meal',
            name='przelicznik',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='meal',
            name='wrazliwosc',
            field=models.FloatField(default=1),
        ),
    ]
