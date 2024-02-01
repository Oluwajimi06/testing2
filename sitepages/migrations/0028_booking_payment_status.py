# Generated by Django 4.2.7 on 2024-01-30 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepages', '0027_table_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
    ]
