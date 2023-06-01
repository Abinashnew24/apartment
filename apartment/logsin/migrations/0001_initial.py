# Generated by Django 4.2.1 on 2023-05-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('author', models.CharField(default='Guest', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('description', models.TextField(default='Available in LictLibrary')),
            ],
        ),
    ]
