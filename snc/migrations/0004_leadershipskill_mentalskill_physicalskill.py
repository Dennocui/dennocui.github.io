# Generated by Django 2.2.5 on 2019-11-14 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0010_delete_playerskill'),
        ('snc', '0003_tacticleskill'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhysicalSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Body Weight')),
                ('bench_press', models.IntegerField(verbose_name='Bench Press(1RM)')),
                ('bent_over_row', models.IntegerField(verbose_name='Bent Over Row')),
                ('deadlift', models.IntegerField(verbose_name='Deadlift')),
                ('squats', models.IntegerField(verbose_name='Squarts')),
                ('m10', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='10M Sprints')),
                ('m40', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='40M Sprints')),
                ('yoyo', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Yoyo')),
                ('physical_commment', models.TextField(verbose_name='Commments')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Date Created')),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player')),
            ],
        ),
        migrations.CreateModel(
            name='MentalSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_drive', models.CharField(choices=[('1', 'Work On'), ('2', 'Adequate'), ('3', 'Excellent')], default='1', max_length=15, verbose_name='Self Drive')),
                ('readiness', models.CharField(choices=[('1', 'Work On'), ('2', 'Adequate'), ('3', 'Excellent')], default='1', max_length=15, verbose_name='Performance Readiness')),
                ('focus', models.CharField(choices=[('1', 'Work On'), ('2', 'Adequate'), ('3', 'Excellent')], default='1', max_length=15, verbose_name='Perfomance Focus')),
                ('review', models.CharField(choices=[('1', 'Work On'), ('2', 'Adequate'), ('3', 'Excellent')], default='1', max_length=15, verbose_name='Perfomance Review')),
                ('resilience', models.CharField(choices=[('1', 'Work On'), ('2', 'Adequate'), ('3', 'Excellent')], default='1', max_length=15, verbose_name='Resilience')),
                ('work_ethic', models.CharField(choices=[('1', 'Work On'), ('2', 'Adequate'), ('3', 'Excellent')], default='1', max_length=15, verbose_name='Work Ethic')),
                ('mental_commment', models.TextField(verbose_name='Commments')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Date Created')),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player')),
            ],
        ),
        migrations.CreateModel(
            name='LeadershipSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_awareness', models.CharField(choices=[('1', 'Work On'), ('2', 'Adequate'), ('3', 'Excellent')], default='1', max_length=15, verbose_name='Self Awareness')),
                ('other_awareness', models.CharField(choices=[('1', 'Work On'), ('2', 'Adequate'), ('3', 'Excellent')], default='1', max_length=15, verbose_name='Awareness of others')),
                ('self_reliance', models.CharField(choices=[('1', 'Work On'), ('2', 'Adequate'), ('3', 'Excellent')], default='1', max_length=15, verbose_name='Self Reliance')),
                ('life_balance', models.CharField(choices=[('1', 'Work On'), ('2', 'Adequate'), ('3', 'Excellent')], default='1', max_length=15, verbose_name='Life balance')),
                ('leadership_commment', models.TextField(verbose_name='Commments')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Date Created')),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player')),
            ],
        ),
    ]
