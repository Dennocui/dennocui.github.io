# Generated by Django 2.2.5 on 2019-11-13 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='injury',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='injury',
            name='notes',
            field=models.TextField(null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='injury',
            name='injury_serverity',
            field=models.CharField(choices=[('1', 'Minimal'), ('2', 'Mild'), ('3', 'Moderate'), ('4', 'Severe')], default='1', max_length=2, verbose_name='Injury Serverity'),
        ),
        migrations.AlterField(
            model_name='injury',
            name='injury_type',
            field=models.CharField(max_length=225, verbose_name='Injury Type'),
        ),
    ]
