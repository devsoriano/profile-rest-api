# Generated by Django 2.2 on 2021-02-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0050_externaldistance'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialschemeproject',
            name='replaces',
            field=models.IntegerField(null=True),
        ),
    ]