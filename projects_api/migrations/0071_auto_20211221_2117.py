# Generated by Django 2.2 on 2021-12-22 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0070_auto_20211214_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialschemeproject',
            name='quantity',
            field=models.DecimalField(decimal_places=4, max_digits=30, null=True),
        ),
    ]