# Generated by Django 4.2.4 on 2024-02-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectmodel',
            name='weighted_grade_point',
            field=models.FloatField(default=0.0),
        ),
    ]
