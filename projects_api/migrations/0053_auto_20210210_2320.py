# Generated by Django 2.2 on 2021-02-11 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0052_auto_20210210_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialschemeproject',
            name='comercial_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='materialschemeprojectorigianal',
            name='citi_id_end',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materialschemeprojectorigianal_requests_created', to='projects_api.City'),
        ),
        migrations.AddField(
            model_name='materialschemeprojectorigianal',
            name='city_id_origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.City'),
        ),
        migrations.AddField(
            model_name='materialschemeprojectorigianal',
            name='comercial_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='materialschemeprojectorigianal',
            name='replaces',
            field=models.IntegerField(null=True),
        ),
    ]