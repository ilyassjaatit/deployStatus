# Generated by Django 4.0.3 on 2022-07-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_deployment_github_created_deployment_github_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='github_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]