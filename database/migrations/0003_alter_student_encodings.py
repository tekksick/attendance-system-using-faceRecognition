# Generated by Django 4.2.7 on 2023-11-09 16:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_student_encodings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Encodings',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=10, max_digits=11), blank=True, null=True, size=None),
        ),
    ]
