# Generated by Django 5.1.2 on 2024-11-11 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_alter_package_image_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='activities',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='flights',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='hotels',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
