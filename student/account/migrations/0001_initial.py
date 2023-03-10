# Generated by Django 3.2.16 on 2022-12-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('duration', models.IntegerField()),
                ('fee', models.IntegerField()),
                ('image', models.ImageField(upload_to='pic')),
            ],
        ),
    ]
