# Generated by Django 4.0.4 on 2022-06-01 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=35)),
                ('age', models.IntegerField(default=0)),
                ('date_of_birth', models.DateField()),
                ('years_active', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
                ('name_of_leader', models.CharField(max_length=35)),
                ('number_of_artists', models.IntegerField(default=0)),
                ('date_of_founding', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=35)),
                ('location', models.CharField(max_length=35)),
                ('time_start', models.DateField()),
                ('time_end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=35)),
                ('city', models.CharField(max_length=35)),
                ('country', models.CharField(max_length=35)),
                ('date', models.DateField()),
                ('music_genre', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=25)),
                ('place_of_founding', models.CharField(max_length=35)),
                ('date_of_founding', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=25)),
                ('producer', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number_of_seats', models.IntegerField(default=0)),
                ('number_of_standing_room', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0)),
                ('price', models.FloatField()),
                ('discount', models.CharField(max_length=35)),
                ('ticket_type', models.CharField(max_length=35)),
                ('ticket_number_sold', models.IntegerField(default=0)),
                ('ticket_number_available', models.IntegerField(default=0)),
            ],
        ),
    ]
