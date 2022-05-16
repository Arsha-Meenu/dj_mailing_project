# Generated by Django 4.0.4 on 2022-05-11 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]
