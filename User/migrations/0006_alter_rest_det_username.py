# Generated by Django 5.1.7 on 2025-04-18 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_rename_username_field_rest_det_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rest_det',
            name='username',
            field=models.CharField(max_length=75, unique=True),
        ),
    ]
