# Generated by Django 2.2 on 2022-01-17 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0071_auto_20211221_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructivesystemelement',
            name='quantity',
            field=models.DecimalField(decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='electricityconsumptiondata',
            name='quantity',
            field=models.DecimalField(decimal_places=10, max_digits=20, null=True),
        ),
    ]
