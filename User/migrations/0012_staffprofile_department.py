# Generated by Django 5.1.7 on 2025-05-09 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_rename_contact_number_regularuserprofile_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffprofile',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
