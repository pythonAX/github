# Generated by Django 2.1.8 on 2020-06-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=64, unique=True)),
                ('makr', models.IntegerField()),
            ],
        ),
    ]
