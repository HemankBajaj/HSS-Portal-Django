# Generated by Django 4.2 on 2023-04-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_slot_candidatelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='exptStatus',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('paid ', 'Paid '), ('rejected', 'Rejected')], default='pending', max_length=30),
        ),
    ]