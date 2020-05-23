# Generated by Django 2.2.10 on 2020-05-22 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200522_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Konto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sifra_konta', models.FloatField(default=0.0)),
                ('naziv', models.CharField(default='Konto1', max_length=50)),
                ('glavna_knjiga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GlavnaKnjiga_id12_id_id', to='core.GlavnaKnjiga')),
            ],
        ),
    ]
