# Generated by Django 2.2.10 on 2020-06-01 07:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200601_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenderi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
                ('datum_isteka', models.DateField()),
                ('datum_objave', models.DateField()),
                ('prvi', models.CharField(max_length=255)),
                ('drugi', models.CharField(max_length=255)),
                ('pdf', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Projekti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
                ('sifra', models.IntegerField(max_length=10)),
                ('datum_planiranog_kraja', models.DateField()),
                ('narucilac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Partner')),
            ],
        ),
        migrations.CreateModel(
            name='Obavijesti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opisObavijesti', models.CharField(max_length=60)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blagajna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum_obracuna', models.DateField()),
                ('blagajnik', models.CharField(max_length=55)),
                ('iznosPDV', models.FloatField(default=0.0)),
                ('iznosBezPDV', models.FloatField(default=0.0)),
                ('sifra_racuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Racun')),
            ],
        ),
    ]
