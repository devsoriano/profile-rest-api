# Generated by Django 2.2 on 2021-05-27 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0060_auto_20210520_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialschemeproject',
            name='state_id_origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.State'),
        ),
    ]