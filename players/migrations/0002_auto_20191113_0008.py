# Generated by Django 2.2.5 on 2019-11-12 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='birth_cert_no',
        ),
        migrations.RemoveField(
            model_name='player',
            name='birth_cert_pdf',
        ),
        migrations.RemoveField(
            model_name='player',
            name='check_cert',
        ),
        migrations.RemoveField(
            model_name='player',
            name='check_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='check_passport',
        ),
        migrations.RemoveField(
            model_name='player',
            name='height',
        ),
        migrations.RemoveField(
            model_name='player',
            name='id_image',
        ),
        migrations.RemoveField(
            model_name='player',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='player',
            name='injury_history',
        ),
        migrations.RemoveField(
            model_name='player',
            name='passport',
        ),
        migrations.RemoveField(
            model_name='player',
            name='passport_image',
        ),
        migrations.RemoveField(
            model_name='player',
            name='position',
        ),
        migrations.RemoveField(
            model_name='player',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='player',
            name='weight',
        ),
    ]
