# Generated by Django 4.1.1 on 2022-09-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_experience_candidate_email_candidate_experience_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='resume',
            field=models.BinaryField(),
        ),
    ]