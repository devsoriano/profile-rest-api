# Generated by Django 2.2 on 2021-02-18 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0053_auto_20210210_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materialschemeproject',
            old_name='citi_id_end',
            new_name='city_id_end',
        ),
        migrations.RenameField(
            model_name='materialschemeproject',
            old_name='distanceEnd',
            new_name='distance_end',
        ),
        migrations.RenameField(
            model_name='materialschemeproject',
            old_name='distanceInit',
            new_name='distance_init',
        ),
        migrations.RenameField(
            model_name='materialschemeprojectorigianal',
            old_name='distanceEnd',
            new_name='distance_end',
        ),
        migrations.RenameField(
            model_name='materialschemeprojectorigianal',
            old_name='distanceInit',
            new_name='distance_init',
        ),
    ]
