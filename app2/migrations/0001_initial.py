# Generated by Django 3.2.6 on 2021-09-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Email_id', models.EmailField(max_length=100)),
                ('Password', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]
