# Generated by Django 3.2.8 on 2021-10-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nmae', models.CharField(max_length=70)),
                ('Email', models.EmailField(max_length=70)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
