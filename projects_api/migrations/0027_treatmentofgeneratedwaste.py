# Generated by Django 2.2 on 2020-12-04 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0026_electricityconsumptiondeconstructiveprocess'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentOfGeneratedWaste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landfill', models.IntegerField(null=True)),
                ('recycling', models.IntegerField(null=True)),
                ('reuse', models.IntegerField(null=True)),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.Project')),
                ('section_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.Section')),
            ],
        ),
    ]