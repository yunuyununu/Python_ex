# Generated by Django 5.0.1 on 2024-01-26 00:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('writer', models.CharField(blank=True, max_length=50, null=True)),
                ('memo', models.CharField(blank=True, max_length=2000, null=True)),
                ('post_date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
