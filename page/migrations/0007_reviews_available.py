# Generated by Django 4.0.1 on 2022-01-14 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
