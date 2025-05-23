# Generated by Django 5.1.6 on 2025-03-13 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='city',
            field=models.CharField(default='City', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='email',
            field=models.TextField(default='Email Address'),
        ),
        migrations.AddField(
            model_name='resume',
            name='first_name',
            field=models.CharField(default='First name', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='last_name',
            field=models.CharField(default='Last name', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='phone_number',
            field=models.CharField(default='Phone number', max_length=20),
        ),
        migrations.AlterField(
            model_name='resume',
            name='job_title',
            field=models.CharField(default='Job title', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ResumeSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField(default=0)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='users.resume')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeSubSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='users.resumesection')),
            ],
        ),
    ]
