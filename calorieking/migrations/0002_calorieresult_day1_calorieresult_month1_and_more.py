# Generated by Django 4.2.7 on 2023-12-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorieking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calorieresult',
            name='day1',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='calorieresult',
            name='month1',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='calorieresult',
            name='year1',
            field=models.IntegerField(default=23),
        ),
    ]