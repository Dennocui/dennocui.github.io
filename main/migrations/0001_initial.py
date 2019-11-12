# Generated by Django 2.2.5 on 2019-11-11 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Club Name')),
                ('coach_name', models.CharField(blank=True, max_length=30, verbose_name='Coach Name')),
                ('coach_contact', models.CharField(blank=True, max_length=15, verbose_name='Coach Contact')),
                ('team_manager', models.CharField(blank=True, max_length=30, verbose_name='Team Manager')),
                ('team_manager_contact', models.CharField(blank=True, max_length=15, verbose_name='Team Manager Contact')),
                ('main_grounds', models.CharField(blank=True, max_length=30, null=True, verbose_name='Main Grounds')),
                ('alt_grounds', models.CharField(blank=True, max_length=30, null=True, verbose_name='Alt Grounds')),
                ('region', models.CharField(blank=True, max_length=30, null=True, verbose_name='Club Region')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='club logos', verbose_name='Club Logo')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='High School Name')),
                ('location', models.CharField(max_length=100, verbose_name='School Location')),
                ('patron', models.CharField(max_length=100, verbose_name='School Patron')),
                ('patron_contact', models.CharField(max_length=15, verbose_name='Patron Contact')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Field Position')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClubAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Club')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
