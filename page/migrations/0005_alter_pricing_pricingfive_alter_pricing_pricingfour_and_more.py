# Generated by Django 4.0.1 on 2022-01-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_alter_pricing_pricingfive_alter_pricing_pricingfour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='pricingfive',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='pricingfour',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='pricingsecond',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='pricingthird',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]
