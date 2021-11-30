# Generated by Django 3.2.7 on 2021-11-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inwarding',
            name='inw_category',
            field=models.CharField(choices=[('Permanent - Computer & Peripheral', 'Permanent - Computer & Peripheral'), ('Permanent - Furniture & Fixtures', 'Permanent - Furniture & Fixtures'), ('Permanent - Office Equipment', 'Permanent - Office Equipment'), ('Permanent - Office Renovation', 'Permanent - Office Renovation'), ('Permanent - Motor Vehicle', 'Permanent - Motor Vehicle'), ('Consumables - IT Consumables', 'Consumables - IT Consumables'), ('Consumables - Hygiene', 'Consumables - Hygiene'), ('Consumables - Pantry', 'Consumables - Pantry'), ('Consumables - Stationery', 'Consumables - Stationery')], default='Permanent - Computer & Peripheral', max_length=200),
        ),
        migrations.AlterField(
            model_name='inwarding',
            name='inw_location',
            field=models.CharField(choices=[('Dahra Main Office', 'Dahra Main Office'), ('KNO', 'KNO'), ('ISC', 'ISC'), ('Messaid', 'Messaid')], default='Dahra Main Office', max_length=100),
        ),
        migrations.AlterField(
            model_name='inwarding',
            name='inw_sourcing_department',
            field=models.CharField(choices=[('Management', 'Management'), ('Operations', 'Operations'), ('T&S', 'T&S'), ('E&M', 'E&M'), ('S&S', 'S&S'), ('FCN', 'FCN'), ('NAVAC', 'NAVAC')], default='Management', max_length=200),
        ),
        migrations.AlterField(
            model_name='inwarding',
            name='inw_type',
            field=models.CharField(choices=[('Inventory', 'Inventory'), ('Services', 'Services')], default='Inventory', max_length=200),
        ),
    ]
