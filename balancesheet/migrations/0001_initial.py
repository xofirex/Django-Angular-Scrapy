# Generated by Django 3.0.8 on 2020-07-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(default=None)),
                ('total_assets', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('total_liabilities', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('total_equity', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
            ],
        ),
    ]
