# Generated by Django 4.1.7 on 2023-04-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0005_ticket_address_ticket_ccv_ticket_credit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='exp',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
