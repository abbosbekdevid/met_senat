# Generated by Django 5.0.4 on 2024-04-26 01:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SponsorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('organization', models.CharField(max_length=100)),
                ('sponsor_type', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=40)),
                ('payment_type', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('contract', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='UniversityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudentSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sponsor_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.sponsormodel')),
                ('student_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.studentmodel')),
            ],
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='university_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.universitymodel'),
        ),
    ]
