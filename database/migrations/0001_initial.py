# Generated by Django 4.2.7 on 2023-11-09 16:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('Encodings', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=10, max_digits=11), blank=True, null=True, size=None)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
