# Generated by Django 4.0.4 on 2022-05-20 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listinganimals', '0003_rename_animals_animal'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('animalname', models.CharField(max_length=128)),
                ('breedName', models.CharField(max_length=128)),
            ],
        ),
    ]