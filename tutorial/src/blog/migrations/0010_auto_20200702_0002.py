# Generated by Django 3.0.3 on 2020-07-02 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200701_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]