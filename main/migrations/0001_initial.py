# Generated by Django 5.0.6 on 2024-07-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('area_id', models.CharField(max_length=64)),
                ('area_name', models.CharField(max_length=128)),
                ('data_updated', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
    ]
