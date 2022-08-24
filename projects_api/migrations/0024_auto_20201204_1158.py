# Generated by Django 2.2 on 2020-12-04 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0023_auto_20201204_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricityConsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('percentage', models.IntegerField()),
                ('annual_consumption_required_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.AnnualConsumptionRequired')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.TypeEnergy')),
                ('unit_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.Unit')),
            ],
        ),
        migrations.DeleteModel(
            name='ElectricityConsumption',
        ),
    ]