# Generated by Django 3.0.7 on 2020-06-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('birth', models.CharField(max_length=15)),
                ('death', models.CharField(max_length=15)),
                ('hair', models.CharField(max_length=30)),
                ('height', models.CharField(max_length=30)),
                ('race', models.CharField(max_length=30)),
                ('realm', models.CharField(max_length=50)),
                ('spouse', models.CharField(max_length=40)),
            ],
        ),
    ]