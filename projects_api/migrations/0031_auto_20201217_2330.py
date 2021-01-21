# Generated by Django 2.2 on 2020-12-18 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0030_auto_20201217_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualconsumptionrequired',
            name='project_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Project'),
        ),
        migrations.AlterField(
            model_name='annualconsumptionrequired',
            name='unit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Unit'),
        ),
        migrations.AlterField(
            model_name='constructivesystemelement',
            name='bulk_unit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.BulkUnit'),
        ),
        migrations.AlterField(
            model_name='constructivesystemelement',
            name='constructive_process_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.ConstructiveProcess'),
        ),
        migrations.AlterField(
            model_name='constructivesystemelement',
            name='energy_unit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.EnergyUnit'),
        ),
        migrations.AlterField(
            model_name='constructivesystemelement',
            name='project_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Project'),
        ),
        migrations.AlterField(
            model_name='constructivesystemelement',
            name='section_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Section'),
        ),
        migrations.AlterField(
            model_name='constructivesystemelement',
            name='source_information_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.SourceInformation'),
        ),
        migrations.AlterField(
            model_name='constructivesystemelement',
            name='volume_unit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.VolumeUnit'),
        ),
        migrations.AlterField(
            model_name='electricityconsumptiondata',
            name='annual_consumption_required_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.AnnualConsumptionRequired'),
        ),
        migrations.AlterField(
            model_name='electricityconsumptiondata',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.TypeEnergy'),
        ),
        migrations.AlterField(
            model_name='electricityconsumptiondata',
            name='unit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Unit'),
        ),
        migrations.AlterField(
            model_name='electricityconsumptiondeconstructiveprocess',
            name='project_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Project'),
        ),
        migrations.AlterField(
            model_name='electricityconsumptiondeconstructiveprocess',
            name='section_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Section'),
        ),
        migrations.AlterField(
            model_name='electricityconsumptiondeconstructiveprocess',
            name='source_information_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.SourceInformation'),
        ),
        migrations.AlterField(
            model_name='electricityconsumptiondeconstructiveprocess',
            name='unit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Unit'),
        ),
        migrations.AlterField(
            model_name='material',
            name='unit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Unit'),
        ),
        migrations.AlterField(
            model_name='materialschemedata',
            name='material_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Material'),
        ),
        migrations.AlterField(
            model_name='materialschemedata',
            name='potential_type_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.PotentialType'),
        ),
        migrations.AlterField(
            model_name='materialschemedata',
            name='standard_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Standard'),
        ),
        migrations.AlterField(
            model_name='materialschemedata',
            name='unit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Unit'),
        ),
        migrations.AlterField(
            model_name='materialschemeproject',
            name='material_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Material'),
        ),
        migrations.AlterField(
            model_name='materialschemeproject',
            name='origin_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Origin'),
        ),
        migrations.AlterField(
            model_name='materialschemeproject',
            name='project_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Project'),
        ),
        migrations.AlterField(
            model_name='materialschemeproject',
            name='section_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Section'),
        ),
        migrations.AlterField(
            model_name='sourceinformationdata',
            name='potential_type_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.PotentialType'),
        ),
        migrations.AlterField(
            model_name='sourceinformationdata',
            name='sourceInformarion_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.SourceInformation'),
        ),
        migrations.AlterField(
            model_name='sourceinformationdata',
            name='unit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Unit'),
        ),
        migrations.AlterField(
            model_name='stageschemedata',
            name='unit_stage_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Unit'),
        ),
        migrations.AlterField(
            model_name='treatmentofgeneratedwaste',
            name='project_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Project'),
        ),
        migrations.AlterField(
            model_name='treatmentofgeneratedwaste',
            name='section_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Section'),
        ),
        migrations.AlterField(
            model_name='typeenergydata',
            name='potential_type_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.PotentialType'),
        ),
        migrations.AlterField(
            model_name='typeenergydata',
            name='type_energy_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.TypeEnergy'),
        ),
        migrations.AlterField(
            model_name='typeenergydata',
            name='unit_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.Unit'),
        ),
    ]