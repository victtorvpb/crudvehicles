# Generated by Django 2.0.3 on 2018-03-31 03:44

import apps.crudvehicles.choices
import dj.choices.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudvehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model', dj.choices.fields.ChoiceField(choices=apps.crudvehicles.choices.ModelsTypesChoices, default=2)),
                ('engine', models.FloatField()),
                ('automaker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='autoMaker', to='crudvehicles.AutoMaker')),
            ],
        ),
    ]