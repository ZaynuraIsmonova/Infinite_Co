# Generated by Django 4.2.5 on 2023-09-06 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbilitiesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('percent', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='home_images/')),
            ],
        ),
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='PartnersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='partners/')),
            ],
        ),
        migrations.CreateModel(
            name='PortfoliosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='projects/')),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ServicesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=700)),
                ('icons', models.CharField(max_length=500)),
            ],
        ),
    ]
