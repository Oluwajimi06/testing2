# Generated by Django 4.2.7 on 2024-01-31 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepages', '0031_alter_purchase_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]