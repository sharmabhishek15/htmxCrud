# Generated by Django 4.0.4 on 2022-05-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listinganimals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animals',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='breed',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
