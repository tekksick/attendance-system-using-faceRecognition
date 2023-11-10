# Generated by Django 4.2.7 on 2023-11-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=10)),
                ('years', models.CharField(max_length=50)),
                ('branches', models.CharField(max_length=50)),
            ],
        ),
    ]
