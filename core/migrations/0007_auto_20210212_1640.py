# Generated by Django 3.1.3 on 2021-02-12 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_subscription_tracking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='tracking',
        ),
        migrations.CreateModel(
            name='MonthlyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, unique_for_month=True)),
                ('tracking', models.CharField(blank=True, max_length=50)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subscription')),
            ],
        ),
    ]