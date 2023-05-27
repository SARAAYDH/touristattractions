# Generated by Django 4.1.7 on 2023-05-18 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_attractions', '0002_alter_attraction_homestate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='homeState',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourist_attractions.state', verbose_name='Home State'),
        ),
        migrations.AlterField(
            model_name='state',
            name='stateAbbreviation',
            field=models.CharField(max_length=3, verbose_name='State Abbreviation'),
        ),
        migrations.AlterField(
            model_name='state',
            name='stateName',
            field=models.CharField(max_length=50, verbose_name='State Name'),
        ),
    ]
