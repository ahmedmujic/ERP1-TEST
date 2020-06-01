# Generated by Django 2.2.10 on 2020-05-31 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pozadina',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='asortiman',
            name='cijena_bez_pdv',
            field=models.FloatField(blank=True, default=100, null=True),
        ),
        migrations.AlterField(
            model_name='asortiman',
            name='cijena_s_pdvom',
            field=models.FloatField(blank=True, default=1.0, null=True),
        ),
        migrations.AlterField(
            model_name='asortiman',
            name='kolicina',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='asortiman',
            name='naziv',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='asortiman',
            name='opis',
            field=models.TextField(blank=True, default='ovo je to', null=True),
        ),
        migrations.AlterField(
            model_name='asortiman',
            name='popust',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='asortiman',
            name='sifra',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
