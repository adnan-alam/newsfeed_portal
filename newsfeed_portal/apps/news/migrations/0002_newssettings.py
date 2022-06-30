# Generated by Django 3.2.13 on 2022-06-30 16:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2), size=None)),
                ('source', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=125), size=None)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
            ],
        ),
    ]
