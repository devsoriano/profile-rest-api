# Generated by Django 2.2 on 2021-02-18 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0054_auto_20210217_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materialschemeprojectorigianal',
            old_name='citi_id_end',
            new_name='city_id_end',
        ),
    ]