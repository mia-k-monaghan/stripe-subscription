# Generated by Django 3.1.3 on 2020-12-10 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20201130_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_customer',
            field=models.CharField(blank=True, help_text="The user's Stripe Customer object, if it exists", max_length=100),
        ),
    ]
