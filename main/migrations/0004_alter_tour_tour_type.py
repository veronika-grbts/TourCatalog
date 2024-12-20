# Generated by Django 4.2.16 on 2024-12-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_tour_options_alter_tour_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='tour_type',
            field=models.CharField(choices=[('beach', 'Пляжний'), ('excursion', 'Екскурсійний'), ('ski', 'Гірськолижний'), ('adventure', 'Пригодницький'), ('cruise', 'Круїзний'), ('wellness', 'Оздоровчий'), ('safari', 'Сафарі'), ('culinary', 'Гастрономічний'), ('cultural', 'Культурний'), ('ecotourism', 'Екотуризм')], max_length=50),
        ),
    ]
