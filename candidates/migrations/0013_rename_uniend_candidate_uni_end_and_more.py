# Generated by Django 4.1.1 on 2022-09-22 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0012_candidate_cgpa_candidate_course_candidate_degree_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='uniEnd',
            new_name='uni_end',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='uniStart',
            new_name='uni_start',
        ),
    ]