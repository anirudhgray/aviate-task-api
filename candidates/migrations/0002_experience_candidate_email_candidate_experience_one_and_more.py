# Generated by Django 4.1.1 on 2022-09-21 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=64)),
                ('designation', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('current', models.BooleanField()),
                ('start', models.DateField()),
                ('end', models.DateField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='email',
            field=models.EmailField(default='anirudh@mishra.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='experience_one',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cand', to='candidates.experience'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='experience_two',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='candidates.experience'),
        ),
    ]
