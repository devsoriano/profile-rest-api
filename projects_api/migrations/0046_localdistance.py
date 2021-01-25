# Generated by Django 2.2 on 2021-01-25 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0045_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalDistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(decimal_places=35, max_digits=45, null=True)),
                ('city_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_api.City')),
            ],
        ),
    ]