# Generated by Django 4.0.3 on 2022-07-29 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=255)),
                ('save_members', models.BooleanField(default=False)),
                ('github_id', models.IntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=510)),
                ('description', models.CharField(max_length=510, null=True)),
                ('github_id', models.IntegerField(unique=True)),
                ('save_pull_requests', models.BooleanField(default=False)),
                ('event_tracking', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repos.organization')),
            ],
        ),
        migrations.CreateModel(
            name='PullRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=510)),
                ('github_id', models.BigIntegerField(unique=True)),
                ('url', models.CharField(max_length=510)),
                ('state', models.CharField(max_length=15)),
                ('body', models.TextField(default='', null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('raw_data', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repos.repository')),
            ],
        ),
        migrations.CreateModel(
            name='GithubEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=50)),
                ('github_id', models.BigIntegerField(unique=True)),
                ('pull_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repos.pullrequest')),
            ],
        ),
    ]