# Generated by Django 3.0.3 on 2020-07-04 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zipcode', models.PositiveIntegerField()),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('ethnicity', models.CharField(blank=True, max_length=255, null=True)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('condition', models.TextField(blank=True, null=True)),
                ('sexuality', models.CharField(blank=True, max_length=255, null=True)),
                ('therapy_type', models.CharField(blank=True, max_length=255, null=True)),
                ('modality', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
