# Generated by Django 5.1.6 on 2025-03-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carinfo',
            name='model',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]
