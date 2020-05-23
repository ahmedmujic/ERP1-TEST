# Generated by Django 2.2.10 on 2020-05-22 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200523_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nabavka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField()),
                ('razlog', models.FileField(upload_to='')),
                ('partneri', models.ManyToManyField(blank=True, null=True, to='core.Partner')),
                ('racuni', models.ManyToManyField(to='core.Racun')),
                ('s_ugovor', models.ManyToManyField(blank=True, null=True, to='core.Ugovor')),
            ],
        ),
    ]
