# Generated by Django 5.1.6 on 2025-03-29 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_resume_city_resume_email_resume_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='city',
            field=models.CharField(default='City', max_length=30),
        ),
        migrations.AlterField(
            model_name='resume',
            name='first_name',
            field=models.CharField(default='First name', max_length=30),
        ),
        migrations.AlterField(
            model_name='resume',
            name='job_title',
            field=models.CharField(default='Job title', max_length=30),
        ),
        migrations.AlterField(
            model_name='resume',
            name='last_name',
            field=models.CharField(default='Last name', max_length=30),
        ),
        migrations.AlterField(
            model_name='resumesection',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='resumesection',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='resumesubsection',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='resumesubsection',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
