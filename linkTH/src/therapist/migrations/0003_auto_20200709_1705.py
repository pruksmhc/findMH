# Generated by Django 3.0.3 on 2020-07-09 17:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0002_therapist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapist',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='therapist',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='therapist',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]