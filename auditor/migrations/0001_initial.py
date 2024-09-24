# Generated by Django 5.1.1 on 2024-09-24 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_url', models.CharField(max_length=200)),
                ('call_id', models.CharField(max_length=200)),
                ('audit_datetime', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt_response', models.CharField(max_length=200)),
                ('call_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auditor.call')),
            ],
        ),
    ]
