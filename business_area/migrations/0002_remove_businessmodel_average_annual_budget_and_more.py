# Generated by Django 4.1.3 on 2023-01-27 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_area', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessmodel',
            name='average_annual_budget',
        ),
        migrations.RemoveField(
            model_name='businessmodel',
            name='average_annual_profit',
        ),
        migrations.RemoveField(
            model_name='businessmodel',
            name='business_form',
        ),
        migrations.RemoveField(
            model_name='businessmodel',
            name='business_specialization',
        ),
        migrations.RemoveField(
            model_name='businessmodel',
            name='number_of_employees',
        ),
    ]
