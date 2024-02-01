# Generated by Django 4.2.4 on 2024-02-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('credit_hours', models.IntegerField()),
                ('marks_obtained', models.FloatField()),
            ],
        ),
    ]
