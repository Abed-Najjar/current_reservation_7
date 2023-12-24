# Generated by Django 4.2.8 on 2023-12-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('cid', models.IntegerField(default=0, max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('birthdate', models.DateField()),
            ],
        ),
    ]