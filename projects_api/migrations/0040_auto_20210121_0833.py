# Generated by Django 2.2 on 2021-01-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0039_auto_20210112_0437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electricityconsumptiondata',
            name='percentage',
        ),
        migrations.AddField(
            model_name='electricityconsumptiondata',
            name='source',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
