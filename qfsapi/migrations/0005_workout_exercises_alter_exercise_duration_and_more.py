# Generated by Django 4.2.2 on 2023-06-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qfsapi', '0004_alter_exercise_duration_alter_exercise_iterations_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='exercises',
            field=models.ManyToManyField(related_name='workout_exercises', to='qfsapi.exercise'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='duration',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='iterations',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='rest',
            field=models.IntegerField(default=10),
        ),
    ]
