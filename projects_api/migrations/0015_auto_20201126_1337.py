# Generated by Django 2.2 on 2020-11-26 19:37

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False  # <<<< THIS LINE

    dependencies = [
        ('projects_api', '0014_constructivesystemelement_construction_stage_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConstructionStageType',
            new_name='SourcesElectricityConsumption',
        ),
        migrations.RenameField(
            model_name='sourceselectricityconsumption',
            old_name='name_construction_stage_type',
            new_name='name_source_electricity_consumption',
        ),
        migrations.RemoveField(
            model_name='constructivesystemelement',
            name='construction_stage_type',
        ),
    ]
