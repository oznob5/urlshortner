# Generated by Django 4.0.5 on 2022-06-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=330, verbose_name='Full url address')),
                ('uuid', models.CharField(max_length=10, verbose_name='Short url address')),
            ],
        ),
    ]
