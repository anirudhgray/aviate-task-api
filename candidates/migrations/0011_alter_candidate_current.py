# Generated by Django 4.1.1 on 2022-09-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0010_remove_candidate_experience_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='current',
            field=models.BooleanField(default=False, null=True),
        ),
    ]