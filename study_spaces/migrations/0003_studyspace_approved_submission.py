# Generated by Django 4.2.6 on 2023-10-28 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_spaces', '0002_studyspace_latitude_studyspace_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyspace',
            name='approved_submission',
            field=models.BooleanField(default=False),
        ),
    ]
