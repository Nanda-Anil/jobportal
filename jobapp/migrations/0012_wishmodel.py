# Generated by Django 4.1.4 on 2023-01-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0011_rename_userapply_userapplymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('job', models.CharField(max_length=20)),
                ('jobtype', models.CharField(max_length=20)),
                ('worktype', models.CharField(max_length=20)),
                ('experience', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=20)),
            ],
        ),
    ]
