# Generated by Django 4.1.7 on 2023-04-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0004_ticket_user_alter_artist_social_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='ccv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='credit',
            field=models.CharField(blank=True, max_length=19, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='zipcode',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
