# Generated by Django 4.0.1 on 2022-01-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardtitle', models.CharField(db_index=True, max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pricingfirst', models.CharField(db_index=True, max_length=200)),
                ('pricingsecond', models.CharField(db_index=True, max_length=200)),
                ('pricingthird', models.CharField(db_index=True, max_length=200)),
                ('pricingfour', models.CharField(db_index=True, max_length=200)),
                ('pricingfive', models.CharField(db_index=True, max_length=200)),
            ],
        ),
    ]