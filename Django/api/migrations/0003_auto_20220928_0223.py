# Generated by Django 3.2.15 on 2022-09-28 02:23

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_bikeplusridermodel_cpmodel_environmentmodel_positionmodel_staticmodel_technicalmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DynamicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('long', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('ele', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('distance', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('bearing', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('slope', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='staticmodel',
            name='bike_plus_rider_model',
        ),
        migrations.RemoveField(
            model_name='staticmodel',
            name='cp_model',
        ),
        migrations.RemoveField(
            model_name='staticmodel',
            name='environment_model',
        ),
        migrations.RemoveField(
            model_name='staticmodel',
            name='position_model',
        ),
        migrations.RemoveField(
            model_name='staticmodel',
            name='technical_model',
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='below_steady_state_max_slope',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='below_steady_state_power_usage',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='climbing_cda_increment',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='climbing_min_slope',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='cp',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='crr',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='descending_cda_increment',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='descending_max_slope',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='mass_bike',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='mass_other',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='mass_rider',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='mechanical_efficiency',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='mol_whl_front',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='mol_whl_rear',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='over_threshold_min_slope',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='over_threshold_power_usage',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='starting_distance',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='starting_speed',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='steady_state_power_usage',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='timestep_size',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='w_prime',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='w_prime_recovery_function',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='wheel_radius',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='wind_density',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='wind_direction',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staticmodel',
            name='wind_speed_mps',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BikePlusRiderModel',
        ),
        migrations.DeleteModel(
            name='CPModel',
        ),
        migrations.DeleteModel(
            name='EnvironmentModel',
        ),
        migrations.DeleteModel(
            name='PositionModel',
        ),
        migrations.DeleteModel(
            name='TechnicalModel',
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='dynamic_model',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.dynamicmodel'),
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='static_model',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.staticmodel'),
        ),
    ]
