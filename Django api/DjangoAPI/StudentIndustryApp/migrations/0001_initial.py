# Generated by Django 4.1.8 on 2023-04-08 10:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthData',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=15, unique=True)),
                ('category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Industrialist',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=1)),
                ('company_name', models.CharField(max_length=20)),
                ('about_company', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=25)),
                ('expertise', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('linkedin', models.CharField(max_length=100, unique=True)),
                ('office_mail', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=15)),
                ('job_type', models.CharField(max_length=15)),
                ('working_hours', models.CharField(max_length=15)),
                ('job_description', models.CharField(max_length=100)),
                ('req_skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('req_experience', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=5)),
                ('user_ids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=1)),
                ('batch', models.CharField(max_length=4)),
                ('roll', models.CharField(max_length=8, unique=True)),
                ('department', models.CharField(max_length=25)),
                ('year', models.CharField(max_length=1)),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('description', models.CharField(max_length=200)),
                ('linkedin', models.CharField(max_length=100, unique=True)),
                ('github', models.CharField(max_length=100, unique=True)),
                ('behance', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
