# Generated by Django 4.0.3 on 2022-07-31 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repos', '0003_organization_save_repository'),
    ]

    operations = [
        migrations.CreateModel(
            name='GithubState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_id', models.BigIntegerField(unique=True)),
                ('raw_data', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='githubevent',
            name='raw_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
