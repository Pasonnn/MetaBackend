# Generated by Django 4.2.18 on 2025-05-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
