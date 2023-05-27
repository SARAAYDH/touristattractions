# Generated by Django 4.1.7 on 2023-05-25 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_attractions', '0004_remove_state_stateabbreviation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='homeState',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourist_attractions.state', verbose_name='Home City'),
        ),
        migrations.AlterField(
            model_name='state',
            name='stateName',
            field=models.CharField(max_length=50, verbose_name='City Name'),
        ),
    ]
