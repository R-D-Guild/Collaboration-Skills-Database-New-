# Generated by Django 5.1 on 2024-08-17 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('contact_information', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_per_week', models.IntegerField()),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='availability', to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('skill_type', models.CharField(choices=[('soft', 'Soft Skill'), ('hard', 'Hard Skill')], max_length=10)),
                ('expertise', models.CharField(max_length=100)),
                ('experience_years', models.IntegerField()),
                ('proficiency', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=20)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='members.member')),
            ],
        ),
    ]