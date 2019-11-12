# Generated by Django 2.2.5 on 2019-11-11 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=30, verbose_name='Player Name')),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('kin', models.CharField(max_length=30, verbose_name='Next Of Kin')),
                ('kin_contact', models.CharField(max_length=15, verbose_name='Next Of Kin Contact')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='Address')),
                ('birth_cert_no', models.IntegerField(default=0, verbose_name='Birth Certificate No')),
                ('birth_cert_pdf', models.FileField(blank=True, null=True, upload_to='files/certs', verbose_name='Birth Certificate PDF')),
                ('check_cert', models.BooleanField(default=False, verbose_name='Verify Cert')),
                ('passport', models.CharField(max_length=150, null=True, verbose_name='Passport No')),
                ('passport_image', models.FileField(blank=True, null=True, upload_to='files/passports', verbose_name='Passport PDF')),
                ('check_passport', models.BooleanField(default=False, verbose_name='Verify Passport')),
                ('id_number', models.CharField(max_length=9, null=True, verbose_name='ID No')),
                ('id_image', models.FileField(blank=True, null=True, upload_to='files/ids', verbose_name='ID PDF')),
                ('check_id', models.BooleanField(default=False, verbose_name='Verify Id')),
                ('image', models.ImageField(blank=True, null=True, upload_to='imgages', verbose_name='Player Image')),
                ('allergy', models.CharField(max_length=200, null=True, verbose_name='Allergies')),
                ('injury_history', models.CharField(max_length=225, null=True, verbose_name='Injury History')),
                ('skills', models.CharField(max_length=225, null=True, verbose_name='Player Skills')),
                ('about_player', models.CharField(max_length=225, null=True, verbose_name='About Player')),
                ('tertiary_institution', models.CharField(max_length=50, null=True, verbose_name='Tertiary Institution')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Joined')),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Club')),
                ('high_school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.HighSchool')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Position')),
            ],
        ),
    ]
