# Generated by Django 2.2.10 on 2020-05-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_racun_osnovica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artikal',
            name='kolicina',
        ),
        migrations.RemoveField(
            model_name='usluga',
            name='sati',
        ),
        migrations.AddField(
            model_name='asortiman',
            name='kolicina',
            field=models.FloatField(default=0),
        ),
    ]