# Generated by Django 5.0.3 on 2024-03-24 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LWE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month', models.CharField(max_length=255)),
                ('Quarter_ID', models.FloatField()),
                ('Quarter_Type', models.CharField(max_length=255)),
                ('Elec_Charge', models.FloatField()),
                ('Fixed_Charge', models.FloatField()),
                ('Meter_Rent', models.FloatField()),
                ('Energy_Charge', models.FloatField()),
                ('Total_Charge', models.FloatField()),
            ],
        ),
    ]
