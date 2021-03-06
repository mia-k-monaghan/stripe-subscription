# Generated by Django 3.1.3 on 2020-12-10 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='stripe_customer',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='stripe_subscription',
            field=models.CharField(blank=True, help_text="The user's Stripe Customer object, if it exists", max_length=100),
        ),
    ]
