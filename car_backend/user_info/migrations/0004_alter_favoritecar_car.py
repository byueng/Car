# Generated by Django 5.1.6 on 2025-04-21 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_rename_year_carinfo_age_alter_carinfo_image'),
        ('user_info', '0003_remove_favoritecar_car_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritecar',
            name='car',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='cars.carinfo'),
        ),
    ]
